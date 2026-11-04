# fix_the_functions.py



def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)
# RUNTIME ERROR: NameError - function called before definition
print_header()

def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
# semantic: total was calculated but never returned
        return total
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"




# runtime: user >> username
print(login_line(username="sara", failed=4))
#semantic error need print statement to display the output
print(login_line("omar", 1))




#error 1
#PS C:\Users\mrmaz\Desktop\python-portfolio> & C:\Users\mrmaz\AppData\Local\Python\pythoncore-3.14-64\python.exe c:/Users/mrmaz/Desktop/python-portfolio/functions/fix_the_functions.py
#Traceback (most recent call last):
#  File "c:\Users\mrmaz\Desktop\python-portfolio\functions\fix_the_functions.py", line 2, in <module>
#    print_header()
#    ^^^^^^^^^^^^
#NameError: name 'print_header' is not defined

#error 2
#Traceback (most recent call last):
#  File "c:\Users\mrmaz\Desktop\python-portfolio\functions\fix_the_functions.py", line 26, in <module>
#    print(login_line(user="sara", failed=4))
#          ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
#TypeError: login_line() got an unexpected keyword argument 'user'