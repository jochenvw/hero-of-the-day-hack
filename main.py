#!/usr/bin/env python3
"""
Hero of the Day Hack - Main Entry Point

This is the main entry point for the hackathon project that demonstrates
how to use AI and cloud tools to troubleshoot enterprise networking issues.
"""

import os
import asyncio
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
import typer

# Load environment variables
load_dotenv()

console = Console()
app = typer.Typer()

def display_banner():
    """Display the project banner"""
    banner = """
🚀 Hero of the Day Hack
AI-Powered Enterprise Network Troubleshooting
    """
    console.print(Panel(banner, border_style="blue"))

@app.command()
def main(
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode"),
    config_file: str = typer.Option("config.py", "--config", help="Configuration file path")
):
    """Main entry point for the Hero of the Day Hack application"""
    
    display_banner()
    
    if debug:
        console.print("🐛 Debug mode enabled", style="yellow")
    
    console.print("📋 Starting Hero of the Day Hack...", style="green")
    
    # TODO: Implement the main application logic
    # This is where you'll integrate:
    # - Azure resource investigation
    # - Semantic Kernel for AI reasoning
    # - Network troubleshooting logic
    
    console.print("⚠️  Application logic not yet implemented", style="orange1")
    console.print("🔧 Ready for hackathon development!", style="bold green")

@app.command()
def setup():
    """Set up the development environment"""
    console.print("🔧 Setting up development environment...", style="blue")
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        console.print("📦 Creating virtual environment...", style="yellow")
        os.system("python -m venv venv")
    
    console.print("📥 Installing dependencies...", style="yellow")
    os.system("pip install -r requirements.txt")
    
    console.print("✅ Setup complete! Activate venv with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)", style="green")

@app.command()
def mcp_server():
    """Start the MCP (Model Context Protocol) server for GitHub Copilot integration"""
    console.print("🚀 Starting MCP server for GitHub Copilot...", style="blue")
    
    try:
        from src.mcp_server import run_mcp_server
        run_mcp_server()
    except ImportError as e:
        console.print(f"❌ Error importing MCP server: {e}", style="red")
        console.print("💡 Make sure you have installed the dependencies with: python main.py setup", style="yellow")
    except Exception as e:
        console.print(f"❌ Error running MCP server: {e}", style="red")

if __name__ == "__main__":
    app()