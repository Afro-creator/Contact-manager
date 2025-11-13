class ContactController:
    def __init__(self, data_file):
        self.data_file = data_file
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_contacts(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        return self.contacts

    def delete_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != contact_name]
        self.save_contacts()