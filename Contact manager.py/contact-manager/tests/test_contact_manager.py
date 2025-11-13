import unittest
from src.controllers.contact_controller import ContactController
from src.models.contact import Contact

class TestContactManager(unittest.TestCase):

    def setUp(self):
        self.controller = ContactController()
        self.controller.contacts = []  # Reset contacts for testing

    def test_add_contact(self):
        contact = Contact(name="John Doe", email="john@example.com", phone="1234567890")
        self.controller.add_contact(contact)
        self.assertEqual(len(self.controller.contacts), 1)
        self.assertEqual(self.controller.contacts[0].name, "John Doe")

    def test_view_contacts(self):
        contact1 = Contact(name="John Doe", email="john@example.com", phone="1234567890")
        contact2 = Contact(name="Jane Smith", email="jane@example.com", phone="0987654321")
        self.controller.add_contact(contact1)
        self.controller.add_contact(contact2)
        contacts_list = self.controller.view_contacts()
        self.assertEqual(len(contacts_list), 2)

    def test_delete_contact(self):
        contact = Contact(name="John Doe", email="john@example.com", phone="1234567890")
        self.controller.add_contact(contact)
        self.controller.delete_contact("John Doe")
        self.assertEqual(len(self.controller.contacts), 0)

if __name__ == '__main__':
    unittest.main()