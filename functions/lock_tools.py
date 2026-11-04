#lock_tools.py

def is_locked(failed, max_tries=3):
    """
    It checks the number of failed attempts; if it is greater than or equal to the total number of attempts, it returns a true value.
    """
    return failed >= max_tries

def tries_left(failed, max_tries=3):
    """
    It checks the number of failed attempts; if it is less than the total number of attempts, it returns the number of tries left.
    """
    if is_locked(failed, max_tries):
       return 0
    else:
        return max_tries - failed

def status(failed):
    """
It checks the lock status based on the number of failed attempts.
It returns a value of "locked" if the number of failed attempts exceeds the permitted limit,
and returns "Active" along with the number of remaining attempts if the maximum number of failed attempts has not been reached.
    """
    if is_locked(failed):
        return "locked"
    else:
        return f"active ({tries_left(failed)} tries left)"


print(is_locked(2))

print(is_locked(3))

print(is_locked(3, 5))

print(tries_left(1))

print(tries_left(7))

print(status(1))

print(status(4))