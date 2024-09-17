import re
import logging

def setup_logging(log_file='logs/phonebook.log'):
    """Sets up logging configuration."""
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def validate_phone(phone):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    if not re.match(pattern, phone):
        raise ValueError("Phone number must be in the format (###) ###-####")
    return phone

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if email and not re.match(pattern, email):
        raise ValueError("Invalid email format")
    return email