import re
import datetime
import csv
from collections import defaultdict
import logging

# Setup logging configuration for recording important events and errors
logging.basicConfig(filename='logs/phonebook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Contact:
    """
    A class to represent a contact in a phonebook.

    Attributes:
    ----------
    first_name : str
        The first name of the contact.
    last_name : str
        The last name of the contact.
    phone_number : str
        The contact's phone number (must follow the format (###) ###-####).
    email : str, optional
        The contact's email address.
    address : str, optional
        The contact's home address.
    created_at : datetime
        The timestamp when the contact was created.
    updated_at : datetime
        The timestamp when the contact was last updated.
    """

    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        """
        Initializes a Contact object with the provided attributes.
        
        Parameters:
        ----------
        first_name : str
            The first name of the contact.
        last_name : str
            The last name of the contact.
        phone_number : str
            The contact's phone number, validated for the correct format.
        email : str, optional
            The email of the contact, validated for correct format.
        address : str, optional
            The physical address of the contact.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
    
    def update_contact(self, first_name=None, last_name=None, phone_number=None, email=None, address=None):
        """
        Updates the contact details with new values. If any parameter is None, 
        the respective attribute is not changed.

        Parameters:
        ----------
        first_name : str, optional
            New first name (if provided).
        last_name : str, optional
            New last name (if provided).
        phone_number : str, optional
            New phone number (if provided), validated for correct format.
        email : str, optional
            New email (if provided), validated for correct format.
        address : str, optional
            New physical address (if provided).
        """
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
        """
        String representation of the contact information.
        
        Returns:
        -------
        str:
            Formatted contact details for easy readability.
        """
        return (f'{self.first_name} {self.last_name} | Phone: {self.phone_number} '
                f'| Email: {self.email or "N/A"} | Address: {self.address or "N/A"}')

    def to_dict(self):
        """
        Converts the contact object to a dictionary format, including 
        timestamps for created_at and updated_at.

        Returns:
        -------
        dict:
            Dictionary containing contact details and timestamps.
        """
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
        """
        Validates the phone number format (###) ###-#### using a regular expression.

        Parameters:
        ----------
        phone : str
            The phone number to validate.

        Returns:
        -------
        str:
            Returns the phone number if it matches the required format.

        Raises:
        ------
        ValueError:
            If the phone number does not match the format (###) ###-####.
        """
        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
        if not re.match(pattern, phone):
            raise ValueError("Phone number must be in the format (###) ###-####")
        return phone

    @staticmethod
    def validate_email(email):
        """
        Validates the email format using a regular expression.

        Parameters:
        ----------
        email : str
            The email address to validate.

        Returns:
        -------
        str:
            Returns the email address if it is valid or None if email is not provided.

        Raises:
        ------
        ValueError:
            If the email format is invalid.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if email and not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return email