<div align="center">

#  Password Manager Using Python

**A lightweight, terminal-based password manager built with Python.**  
Store, retrieve, update and delete your website credentials — all from the command line.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)]()

</div>

---

##  Overview

**Password Manager** is a beginner-friendly Python CLI project that demonstrates core programming concepts — file I/O, dictionaries, loops and functions — while solving a real-world problem: managing passwords across multiple websites without a browser.

All credentials are persisted locally in a `passwords.txt` file and loaded into memory at runtime, enabling fast lookups and edits throughout the session.

---

##  Features

|  | Feature | Description |
|---|---------|-------------|
| 1 | **Save** | Store a website and its password |
| 2 | **View All** | Display every saved credential |
| 3 | **Generate** | Create a random 8-character password |
| 4 | **Search** | Find credentials for a specific website |
| 5 | **Update** | Overwrite the password for an existing entry |
| 6 | **Delete** | Remove an entry permanently |
| 7 | **Exit** | Quit the application |

---

##  Project Structure

```
password_manager/
│
├── password_manager.py   # Core application logic
├── passwords.txt         # Auto-generated local credential store
└── README.md             # Project documentation
```

---

##  Getting Started

### Prerequisites

- Python 3.x installed on your system
- No third-party libraries required

Verify your Python installation:

```bash
python --version
```

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/Jay-Deb/password_manager.git

# 2. Navigate into the project directory
cd password_manager

# 3. Run the application
python password_manager.py
```

---

##  Demo

```
----PASSWORD MANAGER----
1. Save password
2. View passwords
3. Generate password
4. Search password
5. Update password
6. Delete password
7. Exit

Enter your choice: 1
Enter the website: github.com
Enter the password: mySecret@123
Password Saved!

Enter your choice: 3
Generated Password: Xk9#mB2!

Enter your choice: 4
Enter website to search: github.com
Password for github.com: mySecret@123
```

---

##  How It Works

1. **On startup** — `passwords.txt` is read and parsed into a Python dictionary (`passwords{}`) for fast in-memory access.
2. **Save (Create)** — New entries are appended to the file and added to the dictionary.
3. **View / Search (Read)** — Data is read directly from the in-memory dictionary.
4. **Update / Delete (Write)** — The dictionary is modified and the entire file is rewritten to stay in sync.

---

##  Security Notice

> This project is built for **learning purposes only.**

- Passwords are stored in **plain text** — do **not** use this for real or sensitive credentials.
- For production-grade security, consider:
  - [`cryptography`](https://pypi.org/project/cryptography/) — Fernet symmetric encryption
  - [`keyring`](https://pypi.org/project/keyring/) — OS-level secure credential storage

---

##  Contributing

Contributions are welcome and appreciated!

```bash
# Fork → Clone → Branch → Commit → Push → Pull Request
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature description"
git push origin feature/your-feature-name
```

Please keep commits clean and descriptive.

---

##  License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Developed by [Jay Deb](https://github.com/Jay-Deb)**  
⭐ Star this repo if you found it useful!

</div>