import random
import string

passwords = {}

try:
    with open("passwords.txt","r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd

except:
    pass

def generate_password():
    char = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(char) for _ in range(8))
    return password

while True :
    print("\n----PASSWORD MANAGER----")
    print("1. Save password")
    print("2. View passwords")
    print("3. Generate password")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        site = input("Enter the website:")
        pwd = input("Enter the password:")
        passwords[site] = pwd

        with open("passwords.txt","a") as file:
            file.write(f"{site}:{pwd}\n")
        print("Password Saved!!")

    elif choice =="2":
        if not passwords:
            print("Empty data!!")
        else:
            for site , pwd in passwords.items():
                print(site,":",pwd)
    
    elif choice == "3":
        print("Password Generated:", generate_password())

    elif choice =="4":
        print("Exitting...")
        break

    else:
        print("Invalid input!!")
