import logging
import csv
import datetime
from collections import defaultdict
from phonebook.contact import Contact

# Configure logging to track important actions and errors
logging.basicConfig(filename='logs/phonebook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PhoneBook:
    """
    A class to manage a phonebook with operations like adding, removing, updating contacts,
    searching, importing from CSV, and more.

    Attributes:
    ----------
    contacts : list
        A list to store Contact objects.
    """

    def __init__(self):
        """
        Initializes an empty PhoneBook instance with an empty contacts list.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Adds a new contact to the phonebook.

        Parameters:
        ----------
        contact : Contact
            The contact to be added.
        """
        self.contacts.append(contact)
        logging.info(f"Added contact: {contact.first_name} {contact.last_name}")

    def remove_contact(self, first_name, last_name):
        """
        Removes a contact from the phonebook by first and last name.

        Parameters:
        ----------
        first_name : str
            The first name of the contact to remove.
        last_name : str
            The last name of the contact to remove.
        """
        self.contacts = [c for c in self.contacts if c.first_name != first_name or c.last_name != last_name]
        logging.info(f"Deleted contact: {first_name} {last_name}")

    def update_contact(self, first_name, last_name, **kwargs):
        """
        Updates an existing contact's details based on the given first and last name.
        Accepts keyword arguments for updating fields like phone number, email, etc.

        Parameters:
        ----------
        first_name : str
            The first name of the contact to update.
        last_name : str
            The last name of the contact to update.
        kwargs : dict
            Fields to be updated (e.g., phone_number, email, address).
        """
        contact = self.find_contact_by_name(first_name, last_name)
        if contact:
            contact.update_contact(**kwargs)
            logging.info(f"Updated contact: {first_name} {last_name}")
        else:
            logging.warning(f"Contact not found for update: {first_name} {last_name}")

    def find_contact_by_name(self, first_name, last_name):
        """
        Finds a contact in the phonebook by first and last name.

        Parameters:
        ----------
        first_name : str
            The first name of the contact to find.
        last_name : str
            The last name of the contact to find.

        Returns:
        -------
        Contact or None:
            The contact object if found, otherwise None.
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        logging.warning(f"Contact not found: {first_name} {last_name}")
        return None

    def search_contacts(self, query):
        """
        Searches contacts by partial matches in the first name, last name, or phone number.

        Parameters:
        ----------
        query : str
            The query string to match against contacts' names or phone numbers.

        Returns:
        -------
        list:
            List of contacts that match the query.
        """
        results = [c for c in self.contacts if query.lower() in c.first_name.lower() 
                   or query.lower() in c.last_name.lower() or query in c.phone_number]
        return results

    def display_all_contacts(self):
        """
        Displays all contacts in the phonebook.
        """
        for contact in self.contacts:
            print(contact)

    def batch_import(self, file_path):
        """
        Imports contacts from a CSV file and adds them to the phonebook.

        Parameters:
        ----------
        file_path : str
            The file path of the CSV file to import contacts from.
        """
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

    def search_by_date_range(self, start_date, end_date):
        """
        Searches for contacts created within a specific date range.

        Parameters:
        ----------
        start_date : str
            The start date (YYYY-MM-DD).
        end_date : str
            The end date (YYYY-MM-DD).

        Returns:
        -------
        list:
            A list of contacts created within the specified date range.
        """
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        results = [c for c in self.contacts if start <= c.created_at <= end]
        return results

    def sort_contacts(self, by='first_name'):
        """
        Sorts contacts by first name or last name.

        Parameters:
        ----------
        by : str, optional
            The field to sort by, either 'first_name' or 'last_name'. Default is 'first_name'.
        """
        if by == 'first_name':
            self.contacts.sort(key=lambda c: c.first_name.lower())
        elif by == 'last_name':
            self.contacts.sort(key=lambda c: c.last_name.lower())
        logging.info(f"Sorted contacts by {by}")

    def group_contacts(self):
        """
        Groups contacts by the first letter of their last name.

        Returns:
        -------
        dict:
            A dictionary with the first letter of last names as keys and lists of contacts as values.
        """
        grouped = defaultdict(list)
        for contact in self.contacts:
            grouped[contact.last_name[0].upper()].append(contact)
        return grouped

    def log_changes(self):
        """
        Displays the log file showing changes made to the phonebook.
        """
        try:
            with open("logs/phonebook.log", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No log file found.")