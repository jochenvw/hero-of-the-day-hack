
# 🚀 Hero of the Day Hack

Welcome to the **Hero of the Day Hack**! This project demonstrates how to use AI and cloud tools to troubleshoot enterprise networking issues in a modern, interactive way. 🌐🤖

## 💼 Business Case & Azure Deployment

**NEW**: Comprehensive business case and cost analysis for Azure deployment is now available in the [`docs/`](./docs/) directory.

### Quick Summary
- **ROI**: 676% annually with 1.5-month payback period
- **Cost**: $894-$1,674/month for production deployment
- **Savings**: $135,912/year through reduced troubleshooting time
- **Architecture**: Secure, scalable Azure deployment with private connectivity

👉 **[View Full Business Case](./docs/README.md)** for detailed cost analysis, architecture diagrams, and deployment templates.

## 📝 Scenario

1. 👤 **Customer** is part of a team that uses the enterprise networking team's deployment stack.
2. 🚀 Customer makes a deployment.
3. ❌ An error occurs during deployment.
4. 💬 Customer asks a question about the issue using GitHub Copilot.
5. 🔍 We investigate the resources in Azure — using Python with Semantic Kernel tools that use Azure Management Python SDK.
6. 🧠 An LLM (Large Language Model) reasons about the potential error.
7. 🗣️ The system responds with a human-readable, interpreted answer.

---

## 🌟 Why This Matters

This workflow shows how AI can help quickly diagnose and resolve cloud deployment issues, making support faster and smarter for everyone! 💡

---

## 🐍 Python Setup

### Quick Start

```bash
git clone <repository-url>
cd hero-of-the-day-hack
pip install -r requirements.txt
python -m src.mcp_server
```

## 🤖 MCP Server Integration

This project includes an MCP (Model Context Protocol) server that enables GitHub Copilot to interact with Azure troubleshooting capabilities.

### Starting the MCP Server

```bash
python main.py mcp-server
```

The MCP server provides the following tools to GitHub Copilot:

- **hello_world**: Test MCP connectivity with a simple greeting
- **get_azure_resource_groups**: List Azure resource groups in your subscription
- **analyze_deployment_error**: Analyze specific deployment errors in Azure
- **get_ai_troubleshooting_advice**: Get AI-powered troubleshooting recommendations via Semantic Kernel
- **get_network_issues**: Analyze network resources for potential issues
- **analyze_azure_resources_with_ai**: AI-powered Azure resource analysis with comprehensive insights
- **list_azure_resources_in_group**: List all resources in a specific resource group

### GitHub Copilot Integration

To use this MCP server with GitHub Copilot, you'll need to configure it in your development environment. The server uses stdio transport for communication.

**Example configuration for GitHub Copilot:**
```json
{
  "mcpServers": {
    "hero-of-the-day": {
      "command": "python",
      "args": ["/path/to/hero-of-the-day-hack/main.py", "mcp-server"],
      "env": {
        "AZURE_SUBSCRIPTION_ID": "your-subscription-id",
        "AZURE_OPENAI_ENDPOINT": "https://your-resource.openai.azure.com/",
        "AZURE_OPENAI_API_KEY": "your-azure-openai-key",
        "AZURE_OPENAI_DEPLOYMENT_NAME": "your-deployment-name"
      }
    }
  }
}
```

### Project Structure

```
📁 hero-of-the-day-hack/
├── 📄 main.py              # Main entry point
├── 📄 requirements.txt     # Python dependencies
├── 📄 .env.example        # Environment variables template
├── 📁 src/                # Source code modules
│   ├── 📄 __init__.py
│   ├── 📄 azure_manager.py  # Azure resource management
│   ├── 📄 ai_agent.py      # AI troubleshooting agent with Semantic Kernel
│   ├── 📄 mcp_server.py    # MCP server for GitHub Copilot
│   └── 📄 config.py        # Configuration management
├── 📁 prompts/            # External system prompts (markdown files)
│   ├── 📄 network_troubleshooting_system.md
│   ├── 📄 azure_resource_analysis.md
│   └── 📄 deployment_error_analysis_template.md
├── 📁 docs/               # Business case and deployment documentation
│   ├── 📄 README.md       # Business case summary
│   ├── 📄 business-case-azure-deployment.md # Detailed cost analysis
│   ├── 📄 azure-architecture.md # Architecture diagrams
│   └── 📄 deployment-guide.md # Infrastructure as Code templates
└── 📄 README.md           # This file
```

### SSL Configuration

**Important**: SSL verification is disabled in this implementation to support traffic intercept scenarios. This is configured at multiple levels:

- Global SSL context in the AI agent
- HTTP client configuration in the MCP server
- Environment settings for Azure SDK clients

This allows the system to work properly in environments where SSL traffic is intercepted and re-signed.

### Azure OpenAI Configuration

The AI agent now uses **Azure OpenAI** instead of regular OpenAI for enhanced security and compliance. Configure the following environment variables:

```bash
# Required Azure OpenAI settings
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_DEPLOYMENT_NAME=your-gpt-4-deployment-name

# Optional API version (defaults to 2024-02-01)
AZURE_OPENAI_API_VERSION=2024-02-01
```

**Benefits of Azure OpenAI:**
- Enterprise-grade security and compliance
- Regional data residency
- Private networking support
- Integration with Azure Active Directory
- SSL bypass compatible with httpx async client

If Azure OpenAI configuration is not provided, the system will gracefully fall back to mock responses for demonstration purposes.

### Key Features

- 🔧 **Azure Integration**: Manage and analyze Azure resources using Azure Management Python SDK
- 🤖 **AI-Powered Analysis**: Use Semantic Kernel for intelligent troubleshooting with external prompt templates
- 🌐 **MCP Server**: Model Context Protocol server for GitHub Copilot integration
- 📝 **External Prompts**: System prompts stored in external markdown files for easy customization
- 🔒 **SSL Bypass**: SSL verification disabled for traffic intercept compatibility
- ⚡ **Quick Setup**: Minimal configuration for rapid hackathon development
- 🎯 **Modular Design**: Easy to extend and customize
- 🛡️ **Error Handling**: Comprehensive fallback mechanisms when services are unavailable

---

Happy hacking! 🎉
