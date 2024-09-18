import logging
import csv
import datetime
from collections import defaultdict
from phonebook.contact import Contact

# Configure logging
logging.basicConfig(filename='phonebook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PhoneBook:
    def __init__(self):
        self.contacts = []

    # Add a contact
    def add_contact(self, contact):
        self.contacts.append(contact)
        logging.info(f"Added contact: {contact.first_name} {contact.last_name}")

    # Remove a contact by first and last name
    def remove_contact(self, first_name, last_name):
        self.contacts = [c for c in self.contacts if c.first_name != first_name or c.last_name != last_name]
        logging.info(f"Deleted contact: {first_name} {last_name}")

    # Update an existing contact
    def update_contact(self, first_name, last_name, **kwargs):
        contact = self.find_contact_by_name(first_name, last_name)
        if contact:
            contact.update_contact(**kwargs)
            logging.info(f"Updated contact: {first_name} {last_name}")
        else:
            logging.warning(f"Contact not found for update: {first_name} {last_name}")

    # Find a contact by first and last name
    def find_contact_by_name(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        logging.warning(f"Contact not found: {first_name} {last_name}")
        return None

    # Search contacts by partial match in name or phone number
    def search_contacts(self, query):
        results = [c for c in self.contacts if query.lower() in c.first_name.lower() 
                   or query.lower() in c.last_name.lower() or query in c.phone_number]
        return results

    # Display all contacts
    def display_all_contacts(self):
        for contact in self.contacts:
            print(contact)

    # Batch import contacts from a CSV file
    def batch_import(self, file_path):
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    contact = Contact(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        phone_number=row['phone_number'],
                        email=row.get('email'),
                        address=row.get('address')
                    )
                    self.add_contact(contact)
                logging.info("Batch import completed.")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            logging.error(f"Error importing file {file_path}: {e}")
            print(f"An error occurred while importing the file: {e}")

    # Search contacts by a date range (based on creation date)
    def search_by_date_range(self, start_date, end_date):
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        results = [c for c in self.contacts if start <= c.created_at <= end]
        return results

    # Sort contacts by first name or last name
    def sort_contacts(self, by='first_name'):
        if by == 'first_name':
            self.contacts.sort(key=lambda c: c.first_name.lower())
        elif by == 'last_name':
            self.contacts.sort(key=lambda c: c.last_name.lower())
        logging.info(f"Sorted contacts by {by}")

    # Group contacts by the first letter of the last name
    def group_contacts(self):
        grouped = defaultdict(list)
        for contact in self.contacts:
            grouped[contact.last_name[0].upper()].append(contact)
        return grouped

    # Display the log of changes
    def log_changes(self):
        try:
            with open("phonebook.log", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No log file found.")