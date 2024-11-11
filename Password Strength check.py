import re
# imports regular expressions

# define function with parameter of password
def strength_test(password):
    if len(password) < 8:
        return False
    # Is password at least 8 characters long

    if not re.search(r'[A-Z]', password):
        return False
    # Does password contain at least 1 upper case letter

    if not re.search(r'[a-z]', password):
        return False
    # Does password contain at least 1 lower case letter

    if not re.search(r'[0-9]',password):
        return False
    # Does password contain at least 1 number

    if not re.search(r'[~!@#$%^&*()_+=<>,.{}]', password):
        return False
    # Does password contain special character
    # I had to tamper with the inputs here, because I used an escape character originally,
    # that was giving a false strong result.


    return True
    # if all conditions are met the password is strong enough.

password = input("Input your password: ")

is_strong = strength_test(password)

if is_strong:
    print("Strong password")
else:
    print("Password is weak")