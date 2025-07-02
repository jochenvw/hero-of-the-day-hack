# Deployment Error Analysis Template

## Error Details
- **Deployment Name**: {{$deployment_name}}
- **Resource Group**: {{$resource_group}}
- **Error State**: {{$deployment_state}}
- **Timestamp**: {{$timestamp}}
- **Error Message**: {{$error_message}}

## Analysis Request
Please analyze the above deployment error and provide:

1. **Root Cause Analysis**
   - What caused this specific error?
   - Are there any prerequisite conditions that weren't met?
   - What Azure service limitations or dependencies are involved?

2. **Detailed Troubleshooting Steps**
   - Step-by-step resolution process
   - Azure CLI or PowerShell commands to investigate
   - Portal navigation instructions
   - Configuration changes needed

3. **Prevention Strategy**
   - How to avoid this error in future deployments
   - Best practices for this type of resource
   - Monitoring and alerting recommendations
   - Infrastructure-as-code improvements

4. **Related Resources**
   - Dependencies that might be affected
   - Resources that should be checked
   - Potential cascading effects

Please provide specific, actionable guidance based on the error context provided.