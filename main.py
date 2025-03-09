#!/usr/bin/env python3
"""
Main entry point for the C2 Platform Email Collection System
"""

import sys
import os
from core.server import app
from dotenv import load_dotenv

def setup_oauth():
    """Set up Google OAuth credentials"""
    # TODO: Implement OAuth setup
    pass

def run_server():
    """Run the Flask server"""
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)

def main():
    # Load environment variables
    load_dotenv()
    
    if len(sys.argv) < 2:
        print("Usage: python main.py [command]")
        print("\nAvailable commands:")
        print("  server         - Run the web server")
        print("  setup-oauth    - Set up Google OAuth credentials")
        print("  admin          - Launch admin dashboard")
        print("  bulk-email     - Send bulk emails")
        print("  template-editor- Edit email templates")
        print("  preview-emails - Preview email templates")
        print("  test-zoho     - Test Zoho email configuration")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "server":
        run_server()
    elif command == "setup-oauth":
        setup_oauth()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()