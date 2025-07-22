## 📇 Command-Line Contact Book Application Project (Python)

A simple yet effective **Contact Book** application that runs in the command-line interface (CLI). This project is developed using **Python** and is designed to allow users to add, search, view contacts directly from the terminal.
---
## 🚀 Features

- 📝 Add a new contact (Name, Phone, Email)
- 🔍 Search contact by name or phone number
- 📋 View all saved contacts
- 💾 Stores contacts in a local `.txt` file
- ✅ Simple and beginner-friendly codebase
---
## 🛠️ Technologies Used

- **Python 3**
- **File Handling (contacts.txt)**
- **Command-line Interface (CLI)**
---

## 📁 Project Structure
contact-book/
├── contact_book.py # Main Python script
├── contacts.txt # Stores contact data (auto-created)
└── README.md # Project documentation

## ▶️ How to Run

1. 📥 Download the repository:
   ```bash
   git clone https://github.com/yourusername/contact-book.git
   cd contact-book
2. ▶️ Run the Python script:
- python contact_book.py
3. 📲 Follow the on-screen menu to use the app.

## 📸 Example Menu (CLI)

===== Contact Book Menu =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Exit
============================
Enter your choice:

## 💡 How It Works
- Contacts are saved in a text file (contacts.txt) in the format:
  Name,Phone,Email
- When you add, the contact is appended to the file.
- View will read and print all stored contacts.
- Search goes line-by-line and matches query with name or phone.
- Delete rewrites the file excluding the matched contact.

## 🎯 Project Use-Cases
- 🧑‍🎓 Ideal for Python beginners
- 📁 Practice file I/O and string handling
- 📞 Can be expanded into a GUI or database-based app

## ✨ Future Enhancements
- 🔒 Password-protected access
- 🗃️ Store contacts in SQLite/MySQL instead of .txt file
- 🌐 Export contacts to CSV or JSON
- 🖼️ Build a GUI using Tkinter or Flask Web Interface
