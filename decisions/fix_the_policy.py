#fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")
#Syntax Error --> (Adding a colon :)
if len(password) < MIN_LENGTH:
    print("- Too short.")
#semantic (use if not elif)
if password == username:
    print("- Same as the username.")
#Semantic --> (Ordering of conditions)
if len(password) >= 16:
    strength = "long"
    
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
#semantic --> (Remove extra space)
print(f"Length: {len(password)} ({strength})")


#Syntax Error
#     File "c:\Users\mrmaz\Desktop\python-portfolio\decisions\fix_the_policy.py", line 8
#    if len(password) < MIN_LENGTH
#                                 ^
#yntaxError: expected ':'