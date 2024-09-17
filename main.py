
from phonebook.phonebook import PhoneBook
from phonebook.contact import Contact
import logging

logging.basicConfig(filename='phonebook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
def main():
    phonebook = PhoneBook()
    
    while True:
        print("\nPhone Book Menu")
        print("1. Add a new contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Sort contacts")
        print("7. Group contacts by last name")
        print("8. Batch import contacts from CSV")
        print("9. Search contacts by date range")
        print("10. View log")
        print("11. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone_number = input("Phone number (###) ###-####: ")
            try:
                Contact.validate_phone(phone_number)
                email = input("Email (optional): ")
                Contact.validate_email(email)
                address = input("Address (optional): ")
                contact = Contact(first_name, last_name, phone_number, email, address)
                phonebook.add_contact(contact)
            except ValueError as e:
                print(e)
        
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
                phonebook.update_contact(first_name, last_name,
                                         phone_number=new_phone_number, email=new_email, address=new_address)
            else:
                print("Contact not found.")
        
        elif choice == "3":
            first_name = input("First name of contact to delete: ")
            last_name = input("Last name: ")
            phonebook.remove_contact(first_name, last_name)
        
        elif choice == "4":
            query = input("Search query: ")
            results = phonebook.search_contacts(query)
            for result in results:
                print(result)
        
        elif choice == "5":
            phonebook.display_all_contacts()
        
        elif choice == "6":
            by = input("Sort by (first_name/last_name): ")
            phonebook.sort_contacts(by)
            phonebook.display_all_contacts()
        
        elif choice == "7":
            grouped_contacts = phonebook.group_contacts()
            for group, contacts in grouped_contacts.items():
                print(f"\n{group}")
                for contact in contacts:
                    print(contact)
        
        elif choice == "8":
            file_path = input("Enter CSV file path: ")
            phonebook.batch_import(file_path)
        
        elif choice == "9":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            results = phonebook.search_by_date_range(start_date, end_date)
            for result in results:
                print(result)
        
        elif choice == "10":
            phonebook.log_changes()
        
        elif choice == "11":
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()