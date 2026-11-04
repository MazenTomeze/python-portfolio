#password_check.py
#fanction to check if the password is long enough and differs from the username
def long_enough(password, minimum=8):
 """
 Checks if a password is long enough.

 """
 return len(password) >= minimum

def differs_from_username(password, username):
  """
  makes sure the password is not the same as the username.

  """
  return password != username

def password_ok(password, username):
  """
  Checks if the password is long enough and differs from the username.
  
  """
  return long_enough(password) and differs_from_username(password, username)

#main program
user_name = input("Username: ")
password = input("Password: ")


if password_ok(password, user_name):
    print("Password accepted.")
else:
    print("Password rejected.")