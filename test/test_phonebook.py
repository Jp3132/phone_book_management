import unittest
from phonebook.phonebook import PhoneBook
from phonebook.contact import Contact

class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()
        self.contact = Contact('John', 'Doe', '(123) 456-7890', 'john.doe@example.com')

    def test_add_contact(self):
        self.phonebook.add_contact(self.contact)
        self.assertEqual(len(self.phonebook.contacts), 1)

    def test_remove_contact(self):
        self.phonebook.add_contact(self.contact)
        self.phonebook.remove_contact('John', 'Doe')
        self.assertEqual(len(self.phonebook.contacts), 0)

if __name__ == '__main__':
    unittest.main()