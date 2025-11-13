def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("Contact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

def prompt_for_contact_info():
    name = input("Enter contact name: ")
    email = input("Enter contact email: ")
    phone = input("Enter contact phone: ")
    return {'name': name, 'email': email, 'phone': phone}

def prompt_for_contact_deletion():
    return input("Enter the name of the contact to delete: ")