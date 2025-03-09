import pytest
from selenium.webdriver.common.by import By

def test_homepage(browser):
    """Test homepage loads correctly"""
    browser.get('http://localhost:5001')
    assert 'C2 Platform' in browser.title

def test_signup_form(browser):
    """Test email signup form"""
    browser.get('http://localhost:5001')
    email_input = browser.find_element(By.ID, 'email')
    submit_button = browser.find_element(By.ID, 'submit')
    
    email_input.send_keys('test@example.com')
    submit_button.click()
    
    success_message = browser.find_element(By.CLASS_NAME, 'success-message')
    assert 'Thank you for subscribing' in success_message.text