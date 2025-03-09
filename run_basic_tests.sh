#!/bin/bash

# Run basic tests script
# This script activates the virtual environment and runs only the basic tests

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

# Kill any existing server processes
echo "Stopping any existing server processes..."
pkill -f "python main.py server" || true
sleep 2

# Start the server in the background
echo "Starting server in the background..."
python main.py server > server.log 2>&1 &
SERVER_PID=$!

# Wait for server to start
echo "Waiting for server to start..."
for i in {1..10}; do
    if curl -s http://localhost:5001 > /dev/null; then
        echo "Server is running!"
        break
    fi
    if [ $i -eq 10 ]; then
        echo "Server failed to start. Check server.log for details."
        exit 1
    fi
    echo "Waiting... ($i/10)"
    sleep 2
done

# Create test_logs directory if it doesn't exist
mkdir -p test_logs