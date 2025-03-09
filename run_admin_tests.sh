#!/bin/bash

# Run admin tests script
# This script activates the virtual environment and runs the admin tests

# Ensure we're in the project root
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install required packages if not already installed
pip install selenium webdriver-manager --quiet