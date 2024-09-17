import unittest
from phonebook.contact import Contact

class TestContact(unittest.TestCase):

    def setUp(self):
        self.contact = Contact('John', 'Doe', '(123) 456-7890', 'john.doe@example.com', '123 Main St')

    def test_contact_creation(self):
        self.assertEqual(self.contact.first_name, 'John')
        self.assertEqual(self.contact.last_name, 'Doe')
        self.assertEqual(self.contact.phone_number, '(123) 456-7890')

    def test_update_contact(self):
        self.contact.update_contact(phone_number='(321) 654-0987')
        self.assertEqual(self.contact.phone_number, '(321) 654-0987')

    def test_invalid_phone_number(self):
        with self.assertRaises(ValueError):
            Contact.validate_phone('123-4567')
            
if __name__ == '__main__':
    unittest.main()