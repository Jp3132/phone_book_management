from phonebook.phonebook import PhoneBook
from phonebook.contact import Contact
import logging

# Configure logging to track user actions
logging.basicConfig(filename='logs/phonebook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function that provides the command-line interface for interacting 
    with the PhoneBook. It displays a menu of options for the user to choose 
    from, such as adding, updating, deleting, searching, and viewing contacts.
    """
    phonebook = PhoneBook()

    while True:
        # Display the phonebook menu
        print("\nPhone Book Menu")
        print("1. Add a new contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Search for a contact (with filtering, sorting, and grouping)")
        print("5. Display all contacts")
        print("6. Batch import contacts from CSV")
        print("7. View log")
        print("8. Exit")

        choice = input("\nSelect an option: ")

        # Add a new contact
        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone_number = input("Phone number (###) ###-####: ")
            try:
                # Validate the phone number format
                Contact.validate_phone(phone_number)
                email = input("Email (optional): ")
                Contact.validate_email(email)  # Validate the email format
                address = input("Address (optional): ")
                # Create and add the contact
                contact = Contact(first_name, last_name, phone_number, email, address)
                phonebook.add_contact(contact)
            except ValueError as e:
                print(e)

        # Update an existing contact
        elif choice == "2":
            first_name = input("First name of contact to update: ")
            last_name = input("Last name: ")
            contact = phonebook.find_contact_by_name(first_name, last_name)
            if contact:
                print("Leave fields blank to keep existing values.")
                new_first_name = input(f"New first name ({contact.first_name}): ") or contact.first_name
                new_last_name = input(f"New last name ({contact.last_name}): ") or contact.last_name
                new_phone_number = input(f"New phone number ({contact.phone_number}): ") or contact.phone_number
                new_email = input(f"New email ({contact.email}): ") or contact.email
                new_address = input(f"New address ({contact.address}): ") or contact.address
                # Update contact with new details
                phonebook.update_contact(first_name, last_name, phone_number=new_phone_number, email=new_email, address=new_address)
            else:
                print("Contact not found.")

        # Delete a contact
        elif choice == "3":
            first_name = input("First name of contact to delete: ")
            last_name = input("Last name: ")
            phonebook.remove_contact(first_name, last_name)

        # Search for a contact with optional filtering, sorting, and grouping
        elif choice == "4":
            search_contacts(phonebook)

        # Display all contacts in the phonebook
        elif choice == "5":
            phonebook.display_all_contacts()

        # Batch import contacts from a CSV file
        elif choice == "6":
            file_path = input("Enter CSV file path: ")
            phonebook.batch_import(file_path)

        # View the log of changes made to the phonebook
        elif choice == "7":
            phonebook.log_changes()

        # Exit the program
        elif choice == "8":
            print("Exiting...")
            break

        # Invalid option
        else:
            print("Invalid option. Try again.")


def search_contacts(phonebook):
    """
    Handles searching for contacts in the phonebook. Provides options for 
    wildcard searching, filtering by date range, sorting by name, and grouping 
    by the first letter of the last name.

    Parameters:
    ----------
    phonebook : PhoneBook
        The PhoneBook instance containing the contacts to search.
    """
    # Step 1: Wildcard Search
    search_query = input("Enter search query (leave blank to skip): ").lower()

    # Step 2: Ask if the user wants to filter by date range
    filter_by_date = input("Would you like to filter by a date range? (y/n): ").lower()
    if filter_by_date == 'y':
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        # Filter contacts by date range
        results = phonebook.search_by_date_range(start_date, end_date)
    else:
        # Perform wildcard search if a query is provided
        if search_query:
            results = phonebook.search_contacts(search_query)
        else:
            results = phonebook.contacts  # No query returns all contacts

    # Step 3: Ask if the user wants to sort the results
    sort_option = input("Sort by (first_name/last_name/none): ").lower()
    if sort_option in ['first_name', 'last_name']:
        phonebook.sort_contacts(by=sort_option)

    # Step 4: Ask if the user wants to group the results by the initial letter of the last name
    group_by_last_name = input("Would you like to group by last name initial? (y/n): ").lower()
    if group_by_last_name == 'y':
        grouped_contacts = phonebook.group_contacts()
        # Display grouped contacts
        for group, contacts in grouped_contacts.items():
            print(f"\n{group}:")
            for contact in contacts:
                print(contact)
    else:
        # Display the sorted or filtered results without grouping
        for contact in results:
            print(contact)


if __name__ == "__main__":
    main()