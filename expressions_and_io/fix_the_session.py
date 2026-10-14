# fix_the_session.py
# This program reports a user's session time.
 
username = input("Username: ")
#Runtime Error -->TypeError: unsupported operand type(s) for /: 'str' and 'int' total_seconds = input("Session length in seconds: ")
total_seconds = int(input("Session length in seconds: "))
#Semantic Error (/) --> (//)
minutes = total_seconds // 60
seconds = total_seconds % 60
print("=" * 30)
#Semantic Error  print("User: {username}")
print(f"User: {username}")
#Runtime Error
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)