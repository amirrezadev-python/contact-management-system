# Contact Management System
contacts = []

def is_duplicate(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return True
    return False

def add_contact():
    name = input("Contact name: ")
    if is_duplicate(name):
        print("Warning: This name already exists!")
        return
    try:
        phone = input("Enter phone number: ")
        if not phone.isdigit():
            print("Warning: Phone number must contain only digits!")
            return
        contacts.append({"name": name, "phone": phone})
        print("Contact added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def show_contacts():
    if not contacts:
        print("The contact list is empty!")
    else:
        print(f"Contact list (Total: {len(contacts)}):")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    name = input("Enter name to search: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found! Name: {contact['name']}, Phone: {contact['phone']}")
            return
    print("Warning: Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            removed = contacts.pop(i)
            print(f"Contact '{removed['name']}' deleted successfully!")
            return
    print("Warning: Contact not found!")

while True:
    print("\nContact Management System")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    try:
        choice = int(input("Choose an option (1-5): "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            show_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Warning: Choose between 1 and 5!")
    except ValueError:
        print("Error: Please enter a valid number!")