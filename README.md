
# 🚀 Hero of the Day Hack

Welcome to the **Hero of the Day Hack**! This project demonstrates how to use AI and cloud tools to troubleshoot enterprise networking issues in a modern, interactive way. 🌐🤖

## 📝 Scenario

1. 👤 **Customer** is part of a team that uses the enterprise networking team's deployment stack.
2. 🚀 Customer makes a deployment.
3. ❌ An error occurs during deployment.
4. 💬 Customer asks a question about the issue using GitHub Copilot.
5. 🔍 We investigate the resources in Azure — using either the MCP server or Python with Semantic Kernel tools.
6. 🧠 An LLM (Large Language Model) reasons about the potential error.
7. 🗣️ The system responds with a human-readable, interpreted answer.

---

## 🌟 Why This Matters

This workflow shows how AI can help quickly diagnose and resolve cloud deployment issues, making support faster and smarter for everyone! 💡

---

## 🐍 Python Setup

### Quick Start

1. **Clone and navigate to the repository:**
   ```bash
   git clone <repository-url>
   cd hero-of-the-day-hack
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your Azure and OpenAI credentials
   ```

4. **Run the application:**
   ```bash
   python main.py --help
   python main.py setup  # Set up development environment
   python main.py        # Run the main application
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
- **get_ai_troubleshooting_advice**: Get AI-powered troubleshooting recommendations
- **get_network_issues**: Analyze network resources for potential issues

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
        "OPENAI_API_KEY": "your-openai-key"
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
│   ├── 📄 ai_agent.py      # AI troubleshooting agent
│   ├── 📄 mcp_server.py    # MCP server for GitHub Copilot
│   └── 📄 config.py        # Configuration management
└── 📄 README.md           # This file
```

### Key Features

- 🔧 **Azure Integration**: Manage and analyze Azure resources
- 🤖 **AI-Powered Analysis**: Use Semantic Kernel for intelligent troubleshooting
- 🌐 **MCP Server**: Model Context Protocol server for GitHub Copilot integration
- ⚡ **Quick Setup**: Minimal configuration for rapid hackathon development
- 🎯 **Modular Design**: Easy to extend and customize

---

Happy hacking! 🎉