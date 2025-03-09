from flask import Blueprint, render_template
import os
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/templates')
@admin_required
def email_templates():
    try:
        # Get all available email templates from the email_templates directory
        base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        templates_dir = os.path.join(base_dir, 'email_templates')
        
        # Create the directory if it doesn't exist
        os.makedirs(templates_dir, exist_ok=True)
        
        # Get all HTML files in the templates directory
        template_files = [f for f in os.listdir(templates_dir) if f.endswith('.html')]
        
        # Import Python templates from email_system
        from email_system.email_templates import EMAIL_TEMPLATES
        
        # Define template types and descriptions
        template_types = {
            'newsletter': 'Regular newsletter sent to subscribers',
            'welcome': 'Welcome email for new subscribers',
            'event': 'Event invitation or announcement',
            'resource_match': 'Notification about matching resources',
            'collaboration': 'Collaboration opportunity notification',
            'waitlist': 'Confirmation of being added to waitlist',
            'contact': 'Response to contact form submission',
            'careers': 'Response to career inquiries',
            'default': 'Default email template'
        }
        
        # Prepare template data from HTML files
        templates = []
        for template_file in template_files:
            template_name = template_file.replace('.html', '')
            templates.append({
                'name': template_name,
                'file': template_file,
                'description': template_types.get(template_name, 'Custom email template'),
                'last_modified': datetime.fromtimestamp(os.path.getmtime(os.path.join(templates_dir, template_file))).strftime('%Y-%m-%d %H:%M:%S'),
                'type': 'html'
            })
        
        return render_template('admin/templates.html', templates=templates)
    except Exception as e:
        return str(e), 500