import os
from typing import List, Dict, Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from jinja2 import Template
from .email_templates import EMAIL_TEMPLATES

def send_welcome_email(recipient_email: str) -> bool:
    """Send welcome email to new subscriber"""
    try:
        template = EMAIL_TEMPLATES['welcome']
        return send_email(
            recipient_email,
            'Welcome to C2 Platform',
            template
        )
    except Exception as e:
        print(f'Error sending welcome email: {e}')
        return False

def send_bulk_email(recipients: List[str], subject: str, template_name: str, context: Dict = None) -> Dict[str, List[str]]:
    """Send bulk emails to multiple recipients"""
    results = {
        'success': [],
        'failed': []
    }
    
    for recipient in recipients:
        try:
            if send_email(recipient, subject, EMAIL_TEMPLATES[template_name], context):
                results['success'].append(recipient)
            else:
                results['failed'].append(recipient)
        except Exception:
            results['failed'].append(recipient)
    
    return results

def send_email(to_email: str, subject: str, template: str, context: Optional[Dict] = None) -> bool:
    """Send a single email using the configured email service"""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = os.environ['EMAIL_SENDER']
        msg['To'] = to_email

        # Render template with context
        if context:
            template = Template(template).render(**context)

        msg.attach(MIMEText(template, 'html'))

        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(os.environ['EMAIL_SENDER'], os.environ['EMAIL_PASSWORD'])
            server.send_message(msg)

        return True
    except Exception as e:
        print(f'Error sending email: {e}')
        return False