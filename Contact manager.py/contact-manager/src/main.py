def main():
    from controllers.contact_controller import ContactController

    # Initialize the contact controller
    contact_controller = ContactController()

    # Load existing contacts
    contact_controller.load_contacts()

    # Start the user interface loop
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            contact_controller.add_contact()
        elif choice == '2':
            contact_controller.view_contacts()
        elif choice == '3':
            contact_controller.delete_contact()
        elif choice == '4':
            contact_controller.save_contacts()
            print("Exiting the contact manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()