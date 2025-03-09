#!/usr/bin/env python3
"""
Frontend tests for the C2 Platform website.
Tests signing up for early access, applying for a position, and sending a message.
Each action should trigger an email to the specified email address.
"""

import time
import argparse
import logging
import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException, 
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging
log_dir = "test_logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"frontend_test_{timestamp}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)