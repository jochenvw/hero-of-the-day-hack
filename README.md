
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
│   └── 📄 config.py        # Configuration management
└── 📄 README.md           # This file
```

### Key Features

- 🔧 **Azure Integration**: Manage and analyze Azure resources
- 🤖 **AI-Powered Analysis**: Use Semantic Kernel for intelligent troubleshooting
- ⚡ **Quick Setup**: Minimal configuration for rapid hackathon development
- 🎯 **Modular Design**: Easy to extend and customize

---

Happy hacking! 🎉