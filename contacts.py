contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
            print("Contact found:")
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of the contact to update: ")
    for contact in contacts:
        if name.lower() == contact['Name'].lower():
            print("Update Contact:")
            print("1. Phone")
            print("2. Email")
            print("3. Address")
            choice = int(input("Enter option to update: "))
            if choice == 1:
                new_phone = input("Enter new phone number: ")
                contact['Phone'] = new_phone
            elif choice == 2:
                new_email = input("Enter new email: ")
                contact['Email'] = new_email
            elif choice == 3:
                new_address = input("Enter new address: ")
                contact['Address'] = new_address
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    for contact in contacts:
        if name.lower() == contact['Name'].lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
