#login_report.py
MAX_LOGIN_ATTEMPTS = 5

user_name = input("Username: ")
failed_attemp = int(input("Failed attempts: "))
attempts_left = MAX_LOGIN_ATTEMPTS - failed_attemp
print ("=" * 30)
print ("LOGIN REPORT")
print ("=" * 30)

print(f"User:\t\t{user_name}")
print(f"Failed:\t\t{failed_attemp}")
print(f"Attempts left:\t{attempts_left}")
#or
#print (f"User:\t\t{user_name}\nFailed:\t\t{failed_attemp}\nAttempts left:\t{attempts_left}")