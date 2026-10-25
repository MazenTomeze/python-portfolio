#login_decision.py
MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

user_name = input("Username: ")
failed = int(input("Failed attempts so far: "))
password = input("Password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif user_name != KNOWN_USER:
    print("Unknown user.")
else:
    if password == STORED_PASSWORD:
        print("Access granted.")
    else:
        attempts_left = MAX_FAILED - failed - 1
        print(f"Access denied. Attempts left: {attempts_left}")