"""
AI Agent Module using Semantic Kernel

This module implements the AI reasoning component for network troubleshooting.
"""

import asyncio
import os
import ssl
from typing import Dict, List, Any
import logging
from pathlib import Path
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.core_plugins.text_plugin import TextPlugin
from semantic_kernel.functions import KernelArguments
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig
from semantic_kernel.functions import KernelFunctionFromPrompt

logger = logging.getLogger(__name__)

# Disable SSL verification globally for traffic intercept scenarios
# This affects all HTTP requests made by the OpenAI client and other components
ssl._create_default_https_context = ssl._create_unverified_context

class NetworkTroubleshootingAgent:
    """AI Agent for network troubleshooting using Semantic Kernel"""
    
    def __init__(self, openai_api_key: str = None, model: str = "gpt-4"):
        self.kernel = Kernel()
        self.model = model
        self.prompts_dir = Path(__file__).parent.parent / "prompts"
        self.deployment_analyzer = None  # Initialize as None
        
        if openai_api_key:
            # Add OpenAI chat completion service with SSL verification disabled
            # Note: SSL verification is handled at the HTTP client level
            chat_completion = OpenAIChatCompletion(
                service_id="chat-gpt",
                ai_model_id=model,
                api_key=openai_api_key
            )
            self.kernel.add_service(chat_completion)
            
            # Add text plugin for basic text operations
            self.kernel.add_plugin(TextPlugin(), plugin_name="TextPlugin")
            
            # Load and register prompt functions
            self._load_prompt_functions()
        else:
            logger.warning("No OpenAI API key provided, AI agent will use fallback responses")
    
    def _load_prompt_functions(self):
        """Load prompt templates from external markdown files"""
        try:
            # Load network troubleshooting system prompt
            system_prompt_path = self.prompts_dir / "network_troubleshooting_system.md"
            if system_prompt_path.exists():
                with open(system_prompt_path, 'r', encoding='utf-8') as f:
                    system_prompt = f.read()
                
                # Load deployment error analysis template
                error_template_path = self.prompts_dir / "deployment_error_analysis_template.md"
                if error_template_path.exists():
                    with open(error_template_path, 'r', encoding='utf-8') as f:
                        error_template = f.read()
                    
                    # Combine system prompt with error analysis template
                    combined_prompt = f"{system_prompt}\n\n{error_template}"
                    
                    # Create prompt template configuration
                    prompt_config = PromptTemplateConfig(
                        template=combined_prompt,
                        name="analyze_deployment_error",
                        description="Analyze Azure deployment errors with expert troubleshooting guidance",
                        input_variables=[
                            InputVariable(name="deployment_name", description="Name of the failed deployment"),
                            InputVariable(name="resource_group", description="Resource group name"),
                            InputVariable(name="deployment_state", description="Current deployment state"),
                            InputVariable(name="timestamp", description="Deployment timestamp"),
                            InputVariable(name="error_message", description="Error message details"),
                        ]
                    )
                    
                    # Register the function with the kernel
                    self.deployment_analyzer = KernelFunctionFromPrompt(
                        function_name="analyze_deployment_error",
                        prompt_template_config=prompt_config
                    )
                    
        except Exception as e:
            logger.error(f"Error loading prompt functions: {e}")
            # Fallback to basic functionality if prompt loading fails
            self.deployment_analyzer = None
    
    async def analyze_deployment_error(self, error_details: Dict[str, Any]) -> str:
        """Analyze deployment error and provide recommendations"""
        
        try:
            # Use Semantic Kernel function if available
            if self.deployment_analyzer and hasattr(self.kernel, 'services') and self.kernel.services:
                # Prepare arguments for the semantic kernel function
                arguments = KernelArguments(
                    deployment_name=error_details.get('deployment_name', 'Unknown'),
                    resource_group=error_details.get('resource_group', 'Unknown'),
                    deployment_state=error_details.get('deployment_state', 'Unknown'),
                    timestamp=str(error_details.get('timestamp', 'Unknown')),
                    error_message=str(error_details.get('error', error_details.get('description', 'No error message provided')))
                )
                
                # Execute the semantic kernel function
                result = await self.kernel.invoke(self.deployment_analyzer, arguments)
                return str(result) if result else self._generate_mock_analysis(error_details)
            else:
                logger.warning("Semantic Kernel not properly configured, using fallback analysis")
                return self._generate_mock_analysis(error_details)
                
        except Exception as e:
            logger.error(f"Error in AI analysis: {e}")
            return f"Error analyzing deployment: {str(e)}\n\nFallback analysis:\n{self._generate_mock_analysis(error_details)}"
    
    def _generate_mock_analysis(self, error_details: Dict[str, Any]) -> str:
        """Generate a mock analysis for demonstration purposes"""
        return f"""
        🔍 **Root Cause Analysis:**
        Based on the deployment error details, this appears to be a network configuration issue.
        
        🛠️ **Troubleshooting Steps:**
        1. Check network security group rules
        2. Verify subnet configuration
        3. Validate DNS settings
        4. Review firewall policies
        
        🔒 **Prevention Recommendations:**
        - Implement infrastructure as code
        - Use Azure Policy for compliance
        - Set up monitoring and alerting
        
        📊 **Error Summary:**
        State: {error_details.get('deployment_state', 'Unknown')}
        Timestamp: {error_details.get('timestamp', 'Unknown')}
        """
    
    async def suggest_next_steps(self, analysis_result: str) -> List[str]:
        """Suggest next steps based on analysis"""
        
        try:
            # Create a simple prompt for next step suggestions
            if hasattr(self.kernel, 'services') and self.kernel.services:
                prompt = f"""
                Based on the following network troubleshooting analysis, suggest 5 specific next steps:
                
                Analysis: {analysis_result}
                
                Provide only the steps as a numbered list, each step should be actionable and specific.
                """
                
                # Create a simple function for next steps
                from semantic_kernel.prompt_template import PromptTemplateConfig
                config = PromptTemplateConfig(
                    template=prompt,
                    name="suggest_next_steps",
                    description="Suggest next troubleshooting steps"
                )
                
                next_steps_function = KernelFunctionFromPrompt(
                    function_name="suggest_next_steps",
                    prompt_template_config=config
                )
                
                result = await self.kernel.invoke(next_steps_function, KernelArguments())
                
                # Parse the result into a list
                if result:
                    lines = str(result).strip().split('\n')
                    steps = [line.strip() for line in lines if line.strip() and any(char.isdigit() for char in line[:3])]
                    return steps if steps else self._get_default_next_steps()
                    
        except Exception as e:
            logger.error(f"Error generating next steps: {e}")
        
        return self._get_default_next_steps()
    
    def _get_default_next_steps(self) -> List[str]:
        """Get default next steps when AI analysis fails"""
        return [
            "Review network security group configuration",
            "Check Azure resource quotas and limits",
            "Validate ARM template syntax",
            "Test connectivity from deployment source",
            "Review diagnostic logs in Azure Monitor"
        ]
    
    async def analyze_azure_resources(self, resource_data: Dict[str, Any]) -> str:
        """Analyze Azure resources using Semantic Kernel with external prompts"""
        
        try:
            # Load Azure resource analysis prompt
            resource_prompt_path = self.prompts_dir / "azure_resource_analysis.md"
            if resource_prompt_path.exists() and hasattr(self.kernel, 'services') and self.kernel.services:
                with open(resource_prompt_path, 'r', encoding='utf-8') as f:
                    system_prompt = f.read()
                
                combined_prompt = f"""
                {system_prompt}
                
                ## Resource Data to Analyze
                {resource_data}
                
                Please provide a comprehensive analysis following the framework outlined above.
                """
                
                # Create prompt template configuration
                config = PromptTemplateConfig(
                    template=combined_prompt,
                    name="analyze_azure_resources",
                    description="Analyze Azure resources and provide insights"
                )
                
                resource_analyzer = KernelFunctionFromPrompt(
                    function_name="analyze_azure_resources",
                    prompt_template_config=config
                )
                
                result = await self.kernel.invoke(resource_analyzer, KernelArguments())
                return str(result) if result else self._generate_mock_resource_analysis(resource_data)
            else:
                logger.warning("Resource analysis prompt not found or Semantic Kernel not configured")
                return self._generate_mock_resource_analysis(resource_data)
                
        except Exception as e:
            logger.error(f"Error in resource analysis: {e}")
            return f"Error analyzing resources: {str(e)}\n\nFallback analysis:\n{self._generate_mock_resource_analysis(resource_data)}"
    
    def _generate_mock_resource_analysis(self, resource_data: Dict[str, Any]) -> str:
        """Generate a mock resource analysis for demonstration purposes"""
        return f"""
        📊 **Azure Resource Analysis Summary**
        
        **Resources Found**: {len(resource_data.get('resources', []))} resources analyzed
        **Resource Groups**: {len(resource_data.get('resource_groups', []))} groups
        
        🔍 **Key Findings**:
        - Network configuration appears standard
        - No immediate security concerns identified
        - Resources are properly distributed
        
        💡 **Recommendations**:
        - Consider implementing Azure Monitor for better visibility
        - Review resource tagging strategy
        - Evaluate cost optimization opportunities
        
        📋 **Next Actions**:
        - Set up monitoring and alerting
        - Review security group configurations
        - Implement backup and disaster recovery
        """