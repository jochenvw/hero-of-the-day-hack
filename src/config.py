"""
Configuration Module

Handles application configuration and environment variables.
"""

import os
from typing import Optional
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@dataclass
class Config:
    """Application configuration"""
    
    # Azure Configuration
    azure_subscription_id: Optional[str] = None
    azure_tenant_id: Optional[str] = None
    azure_client_id: Optional[str] = None
    azure_client_secret: Optional[str] = None
    
    # OpenAI Configuration
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4"
    
    # Application Configuration
    debug: bool = False
    log_level: str = "INFO"
    
    def __post_init__(self):
        """Load configuration from environment variables"""
        self.azure_subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID", self.azure_subscription_id)
        self.azure_tenant_id = os.getenv("AZURE_TENANT_ID", self.azure_tenant_id)
        self.azure_client_id = os.getenv("AZURE_CLIENT_ID", self.azure_client_id)
        self.azure_client_secret = os.getenv("AZURE_CLIENT_SECRET", self.azure_client_secret)
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY", self.openai_api_key)
        self.openai_model = os.getenv("OPENAI_MODEL", self.openai_model)
        
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
        self.log_level = os.getenv("LOG_LEVEL", self.log_level)
    
    def validate(self) -> list[str]:
        """Validate configuration and return list of missing required values"""
        missing = []
        
        if not self.azure_subscription_id:
            missing.append("AZURE_SUBSCRIPTION_ID")
        
        if not self.openai_api_key:
            missing.append("OPENAI_API_KEY")
        
        return missing

# Global configuration instance
config = Config()

def get_config() -> Config:
    """Get the global configuration instance"""
    return config