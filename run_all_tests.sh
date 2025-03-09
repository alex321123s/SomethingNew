#!/bin/bash

# Run all tests script
# This script runs all test suites for the C2 Platform

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
echo "Installing required packages..."
pip install selenium webdriver-manager --quiet

# Create test_logs directory if it doesn't exist
mkdir -p test_logs

# Create a timestamp for this test run
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
SUMMARY_LOG="test_logs/all_tests_${TIMESTAMP}.log"

echo "C2 Platform Test Suite" | tee -a $SUMMARY_LOG
echo "======================" | tee -a $SUMMARY_LOG
echo "Started at: $(date)" | tee -a $SUMMARY_LOG
echo "" | tee -a $SUMMARY_LOG

# Run basic tests
echo "Running basic tests..." | tee -a $SUMMARY_LOG
chmod +x run_basic_tests.sh
./run_basic_tests.sh
BASIC_RESULT=$?

if [ $BASIC_RESULT -eq 0 ]; then
    echo "✅ Basic tests PASSED" | tee -a $SUMMARY_LOG
else
    echo "❌ Basic tests FAILED" | tee -a $SUMMARY_LOG
fi
echo "" | tee -a $SUMMARY_LOG

# Run email tests
echo "Running email tests..." | tee -a $SUMMARY_LOG
chmod +x run_email_tests.sh
./run_email_tests.sh
EMAIL_RESULT=$?

if [ $EMAIL_RESULT -eq 0 ]; then
    echo "✅ Email tests PASSED" | tee -a $SUMMARY_LOG
else
    echo "❌ Email tests FAILED" | tee -a $SUMMARY_LOG
fi
echo "" | tee -a $SUMMARY_LOG

# Run admin tests if credentials are provided
if [ $# -eq 2 ]; then
    echo "Running admin tests with provided credentials..." | tee -a $SUMMARY_LOG
    chmod +x run_admin_tests.sh
    ./run_admin_tests.sh "$1" "$2"
    ADMIN_RESULT=$?
    
    if [ $ADMIN_RESULT -eq 0 ]; then
        echo "✅ Admin tests PASSED" | tee -a $SUMMARY_LOG
    else
        echo "❌ Admin tests FAILED" | tee -a $SUMMARY_LOG
    fi
fi