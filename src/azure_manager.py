"""
Azure Integration Module

This module handles interactions with Azure resources for network troubleshooting.
"""

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
import logging

logger = logging.getLogger(__name__)

class AzureManager:
    """Manages Azure resource operations"""
    
    def __init__(self, subscription_id: str = None):
        self.subscription_id = subscription_id
        self.credential = DefaultAzureCredential()
        
        if subscription_id:
            self.resource_client = ResourceManagementClient(
                self.credential, subscription_id
            )
            self.network_client = NetworkManagementClient(
                self.credential, subscription_id
            )
    
    def list_resource_groups(self):
        """List all resource groups in the subscription"""
        try:
            resource_groups = list(self.resource_client.resource_groups.list())
            return [rg.name for rg in resource_groups]
        except Exception as e:
            logger.error(f"Error listing resource groups: {e}")
            return []
    
    def get_network_issues(self, resource_group: str):
        """Analyze network resources for potential issues"""
        # TODO: Implement network analysis logic
        # This is where you would check:
        # - Network security groups
        # - Route tables
        # - Virtual networks
        # - Load balancers
        # - Application gateways
        
        logger.info(f"Analyzing network resources in {resource_group}")
        return {
            "status": "analysis_needed",
            "message": "Network analysis logic to be implemented"
        }
    
    def diagnose_deployment_error(self, deployment_name: str, resource_group: str):
        """Diagnose deployment errors"""
        try:
            # Get deployment details
            deployment = self.resource_client.deployments.get(
                resource_group, deployment_name
            )
            
            return {
                "deployment_name": deployment_name,
                "resource_group": resource_group,
                "deployment_state": deployment.properties.provisioning_state,
                "error": deployment.properties.error if deployment.properties.error else None,
                "timestamp": deployment.properties.timestamp
            }
        except Exception as e:
            logger.error(f"Error getting deployment details: {e}")
            return {"error": str(e)}
    
    def list_resources_in_group(self, resource_group: str):
        """List all resources in a specific resource group"""
        try:
            resources = list(self.resource_client.resources.list_by_resource_group(resource_group))
            resource_list = []
            
            for resource in resources:
                resource_info = {
                    "name": resource.name,
                    "type": resource.type,
                    "location": resource.location,
                    "id": resource.id
                }
                # Add additional properties if available
                if hasattr(resource, 'kind') and resource.kind:
                    resource_info["kind"] = resource.kind
                if hasattr(resource, 'sku') and resource.sku:
                    resource_info["sku"] = resource.sku.name if hasattr(resource.sku, 'name') else str(resource.sku)
                
                resource_list.append(resource_info)
            
            return {
                "resource_group": resource_group,
                "resource_count": len(resource_list),
                "resources": resource_list
            }
            
        except Exception as e:
            logger.error(f"Error listing resources in group {resource_group}: {e}")
            return {"error": str(e), "resource_group": resource_group}