contacts = {
    "Alice": {"phone": "555-0101"},
    "Ben": {"phone": "555-0102"},
}


def show_menu():
    print("\nContact Book Menu")
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Search for a contact")
    print("4. Quit")


# Task 1
def view_contacts(contact_book):
    # Print all contacts in a clear format.
    # Show a helpful message if the contact book is empty.
    pass


# Task 2
def add_contact(contact_book):
    # Ask the user for a name and phone number.
    # Add the new contact to the dictionary.
    pass


# Task 2
def search_contact(contact_book):
    # Ask the user for a name.
    # Show the contact's information if it exists.
    pass


# Task 3
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
