import os

CONTACTS_FILE = 'contacts.txt'

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    
    with open(CONTACTS_FILE, 'a') as f:
        f.write(f"{name},{phone},{email}\n")
    
    print(f"✅ Contact '{name}' added successfully.\n")

def view_contacts():
    with open("contacts.txt", "r") as file:
        print("📋 All Contacts:")
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                print(f"⚠️ Skipping invalid line: {line.strip()}")
                continue
            name, phone, email = parts
            print(f"Name: {name}, Phone: {phone}, Email: {email}")


def search_contacts():
    with open("contacts.txt", "r") as file:
        search_name = input("Enter name to search: ").strip().lower()
        found = False
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue  # skip lines with missing data
            name, phone, email = parts
            if search_name in name.lower():
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
                found = True
        if not found:
            print("Contact not found.")

    if not found:
        print("❌ No matching contacts found.\n")
    else:
        print()

def main():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()

