"""
MCP Server for Hero of the Day Hack

This module implements an MCP (Model Context Protocol) server using FastMCP 
to provide Azure network troubleshooting capabilities to GitHub Copilot.
"""

import asyncio
from typing import Dict, Any, List
import logging
from mcp.server import FastMCP
from .azure_manager import AzureManager
from .ai_agent import NetworkTroubleshootingAgent
from .config import get_config
import httpx

logger = logging.getLogger(__name__)

# Initialize the MCP server
mcp_server = FastMCP(
    name="hero-of-the-day-mcp-server",
    instructions="""
    This is the Hero of the Day MCP server for Azure network troubleshooting.
    
    Available capabilities:
    - Get Azure resource groups
    - Analyze network deployment errors
    - Provide AI-powered troubleshooting recommendations
    
    Use the available tools to investigate Azure network issues and get 
    intelligent recommendations for resolving deployment problems.
    """
)

@mcp_server.tool()
def hello_world(name: str = "World") -> str:
    """
    A simple hello world tool to test MCP connectivity.
    
    Args:
        name: The name to greet (default: "World")
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to the Hero of the Day MCP server! 🚀"

@mcp_server.tool()
def get_azure_resource_groups() -> List[str]:
    """
    Get list of Azure resource groups in the configured subscription.
    
    Returns:
        List of resource group names
    """
    try:
        config = get_config()
        if not config.azure_subscription_id:
            return ["Error: Azure subscription ID not configured"]
        
        azure_manager = AzureManager(config.azure_subscription_id)
        resource_groups = azure_manager.list_resource_groups()
        
        if not resource_groups:
            return ["No resource groups found"]
        
        return resource_groups
    except Exception as e:
        logger.error(f"Error getting resource groups: {e}")
        return [f"Error: {str(e)}"]

@mcp_server.tool()
def analyze_deployment_error(
    deployment_name: str, 
    resource_group: str
) -> Dict[str, Any]:
    """
    Analyze a specific deployment error in Azure.
    
    Args:
        deployment_name: Name of the deployment to analyze
        resource_group: Resource group containing the deployment
        
    Returns:
        Analysis results with error details and recommendations
    """
    try:
        config = get_config()
        if not config.azure_subscription_id:
            return {"error": "Azure subscription ID not configured"}
        
        azure_manager = AzureManager(config.azure_subscription_id)
        deployment_info = azure_manager.diagnose_deployment_error(
            deployment_name, resource_group
        )
        
        return deployment_info
    except Exception as e:
        logger.error(f"Error analyzing deployment: {e}")
        return {"error": str(e)}

@mcp_server.tool()
async def get_ai_troubleshooting_advice(
    error_details: str
) -> str:
    """
    Get AI-powered troubleshooting advice for network issues.
    
    Args:
        error_details: Description of the error or issue
        
    Returns:
        AI-generated troubleshooting advice and recommendations
    """
    try:
        config = get_config()
        if not config.openai_api_key:
            return "Error: OpenAI API key not configured"
        
        ai_agent = NetworkTroubleshootingAgent(
            config.openai_api_key, 
            config.openai_model
        )
        
        # Create a structured error details dict
        error_data = {"description": error_details}
        analysis = await ai_agent.analyze_deployment_error(error_data)
        
        return analysis
    except Exception as e:
        logger.error(f"Error getting AI advice: {e}")
        return f"Error: {str(e)}"

@mcp_server.tool()
def get_network_issues(resource_group: str) -> Dict[str, Any]:
    """
    Analyze network resources in a resource group for potential issues.
    
    Args:
        resource_group: Name of the resource group to analyze
        
    Returns:
        Analysis of network resources and potential issues
    """
    try:
        config = get_config()
        if not config.azure_subscription_id:
            return {"error": "Azure subscription ID not configured"}
        
        azure_manager = AzureManager(config.azure_subscription_id)
        network_analysis = azure_manager.get_network_issues(resource_group)
        
        return network_analysis
    except Exception as e:
        logger.error(f"Error analyzing network issues: {e}")
        return {"error": str(e)}

def run_mcp_server():
    """
    Run the MCP server using streamable-http transport (FastMCP built-in HTTP server).
    This is the main entry point for the MCP server.
    """
    logger.info("Starting Hero of the Day MCP server (streamable-http mode)...")
    # Use a custom HTTP client with SSL verification disabled
    mcp_server.run(transport="streamable-http")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run the server
    run_mcp_server()