from flask import Flask, send_from_directory, render_template, redirect, url_for, request, jsonify
import sqlite3
import os
import datetime
import json
from dotenv import load_dotenv
from flask_cors import CORS

# Import the admin blueprint
from admin.admin_web_interface import admin_bp, init_app

# Import the email service
from email_system.email_service import send_welcome_email

# Load environment variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__, static_folder='../website')
CORS(app)

# Register the admin blueprint
app.register_blueprint(admin_bp, url_prefix='/admin')

# Initialize OAuth with the Flask app
init_app(app)

# Set a secret key for session management
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev_secret_key')

# Ensure the database directory exists
os.makedirs('database', exist_ok=True)

# Admin configuration
ADMIN_EMAILS = [
    'alexander.joseph.bell@gmail.com',  # Alexander's email
]

# Rate limiting configuration (doesn't apply to admins)
MAX_EMAILS_PER_DAY = 5  # Maximum emails per day for regular users

# Database setup
def get_db_connection():
    conn = sqlite3.connect('database/emails.db')
    conn.row_factory = sqlite3.Row
    return conn