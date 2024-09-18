
# Phone Book Management Application

## Overview

The **Phone Book Management Application** is a command-line interface (CLI) tool for managing contacts. It supports a wide range of functionalities including adding, updating, deleting, searching, sorting, and batch importing contacts from CSV files. The app is designed to be user-friendly, with advanced features like wildcard searches, date-based filtering, sorting, and grouping of contacts by the first letter of the last name.

## Features

- **Add Contacts**: Add individual contacts with details like first name, last name, phone number, email, and address.
- **Update Contacts**: Update existing contacts by first name and last name.
- **Delete Contacts**: Remove contacts from the phone book.
- **Search Contacts**: Perform wildcard searches on first names, last names, and phone numbers.
- **Filter by Date Range**: Search for contacts created within a specific date range.
- **Sort Contacts**: Sort contacts by first name or last name.
- **Group Contacts**: Group contacts alphabetically by the first letter of the last name.
- **Batch Import from CSV**: Import multiple contacts from a CSV file.
- **View Log**: Review changes made to the phone book (additions, updates, deletions).
- **Error Handling and Logging**: Tracks operations and errors via a log file (`phonebook.log`).

## Setup

### Requirements

- Python 3.6 or higher

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/phone-book-management.git
   cd phone-book-management
   ```

2. **Install Dependencies** (if required):
   This project doesn’t require external libraries, but if you want to add more features (e.g., for testing or additional CSV handling), you can add them to a `requirements.txt` file and install them:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the CSV File**:
   If you want to import contacts in bulk, prepare a CSV file with the following headers:
   ```csv
   first_name,last_name,phone_number,email,address
   ```
   Example `contacts.csv` file:
   ```csv
   first_name,last_name,phone_number,email,address
   John,Doe,(123) 456-7890,john.doe@example.com,123 Elm St
   Jane,Smith,(234) 567-8901,jane.smith@example.com,456 Oak St
   ```

## Usage

1. **Run the Application**:
   To start the application, run the following command:
   ```bash
   python main.py
   ```

2. **Main Menu**:
   Once the app is running, you'll be presented with a menu of options:
   ```
   Phone Book Menu
   1. Add a new contact
   2. Update a contact
   3. Delete a contact
   4. Search for a contact (with filtering, sorting, and grouping)
   5. Display all contacts
   6. Batch import contacts from CSV
   7. View log
   8. Exit
   ```

### Features

#### 1. Add a New Contact
- The app will prompt you for the contact’s first name, last name, phone number, email, and address.

#### 2. Update a Contact
- You will be asked to enter the first and last name of the contact to update.
- You can then update any field (leave fields blank to keep existing values).

#### 3. Delete a Contact
- Provide the first and last name of the contact to delete it from the phone book.

#### 4. Search for a Contact
- You can search by partial name or phone number.
- Optionally, filter contacts by creation date, sort them by first or last name, and group them by the first letter of the last name.

#### 5. Display All Contacts
- View all contacts in the phone book.

#### 6. Batch Import Contacts
- Import multiple contacts from a CSV file. The file should have the following columns: `first_name`, `last_name`, `phone_number`, `email`, and `address`.

#### 7. View Log
- Displays the log of changes made to the phone book, including additions, updates, and deletions.

### Sample CSV Format:
```csv
first_name,last_name,phone_number,email,address
John,Doe,(123) 456-7890,john.doe@example.com,123 Elm St
Jane,Smith,(234) 567-8901,jane.smith@example.com,456 Oak St
```

### Logging
The application logs all changes to `phonebook.log`:
- **Additions**: Logs when a new contact is added.
- **Updates**: Logs any updates made to contacts.
- **Deletions**: Logs when a contact is deleted.
- **Errors**: Logs any file handling or contact search errors.

## Error Handling
The application includes error handling for:
- Invalid phone numbers and emails.
- File-related issues (e.g., missing CSV files during import).
- Contact not found when trying to update or delete.

## Example Interaction

```
Phone Book Menu
1. Add a new contact
2. Update a contact
3. Delete a contact
4. Search for a contact (with filtering, sorting, and grouping)
5. Display all contacts
6. Batch import contacts from CSV
7. View log
8. Exit
```

To add a new contact, choose option `1`:
```
First name: John
Last name: Doe
Phone number: (123) 456-7890
Email: john.doe@example.com
Address: 123 Elm St
```

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.