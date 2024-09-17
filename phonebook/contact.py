import re
import datetime
import csv
from collections import defaultdict
import logging

# Setup logging
logging.basicConfig(filename='phonebook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Contact:
    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
    
    def update_contact(self, first_name=None, last_name=None, phone_number=None, email=None, address=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        self.updated_at = datetime.datetime.now()

    def __repr__(self):
        return (f'{self.first_name} {self.last_name} | Phone: {self.phone_number} '
                f'| Email: {self.email or "N/A"} | Address: {self.address or "N/A"}')

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
        if not re.match(pattern, phone):
            raise ValueError("Phone number must be in the format (###) ###-####")
        return phone

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if email and not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return email