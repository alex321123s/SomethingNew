import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_login(browser):
    """Test admin login functionality"""
    browser.get('http://localhost:5001/admin')
    assert 'Admin Login' in browser.title

def test_email_templates(browser):
    """Test email template management"""
    browser.get('http://localhost:5001/admin/templates')
    templates = browser.find_elements(By.CLASS_NAME, 'template-item')
    assert len(templates) > 0