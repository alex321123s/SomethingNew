from .email_service import send_welcome_email, send_bulk_email
from .email_templates import EMAIL_TEMPLATES

__all__ = ['send_welcome_email', 'send_bulk_email', 'EMAIL_TEMPLATES']