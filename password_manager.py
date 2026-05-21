# Created Password Manager Using Python
# A simple command-line Password Manager built with Python that lets you securely store, view, search, update and delete passwords
# For different websites — all saved locally in a text file.


import random
import string

passwords = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass


def save_to_file():
    with open("passwords.txt", "w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site}:{pwd}\n")


def generate_password():
    char = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(char) for _ in range(8))
    return password


while True:
    print("\n----PASSWORD MANAGER----")
    print("1. Save password")
    print("2. View passwords")
    print("3. Generate password")
    print("4. Search password")
    print("5. Update password")
    print("6. Delete password")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter the website: ")
        pwd = input("Enter the password: ")
        passwords[site] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Password Saved!")

    elif choice == "2":
        if not passwords:
            print("Empty data!")
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    elif choice == "3":
        print("Generated Password:", generate_password())

    elif choice == "4":
        site = input("Enter website to search: ")
        if site in passwords:
            print(f"Password for {site}: {passwords[site]}")
        else:
            print("Website not found!")

    elif choice == "5":
        site = input("Enter website to update: ")
        if site in passwords:
            new_pwd = input("Enter new password: ")
            passwords[site] = new_pwd
            save_to_file()
            print("Password Updated!")
        else:
            print("Website not found!")

    elif choice == "6":
        site = input("Enter website to delete: ")
        if site in passwords:
            del passwords[site]
            save_to_file()
            print("Password Deleted!")
        else:
            print("Website not found!")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid input!")