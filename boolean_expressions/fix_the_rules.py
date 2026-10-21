# fix_the_rules.py
# This program checks a connection against three rules.
role = input("Role: ")
#--> runtime Error
port = int(input("Port: "))
#--> semantic Error
is_admin = role == "admin"
#--> SyntaxError
is_system_port = port <= 1023
#--> semantic Error
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")



# Error 1
# File "c:\Users\mrmaz\Desktop\python-portfolio\boolean_expressions\fix_the_rules.py", line 6
#    is_system_port = port =< 1023
#                           ^
#SyntaxError: invalid syntax


# Error 2
# File "c:\Users\mrmaz\Desktop\python-portfolio\boolean_expressions\fix_the_rules.py", line 6, in <module>
#    is_system_port = port <= 1023 #--> #SyntaxError
#                     ^^^^^^^^^^^^
#TypeError: '<=' not supported between instances of 'str' and 'int'
