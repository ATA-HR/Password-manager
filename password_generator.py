import string
import secrets
import pyperclip


def pass_gen():
    password_lenght = 12
    alphabet = string.ascii_letters + string.digits + ' $@!?~' 
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(password_lenght))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
                and any(c.isspace() for c in password[:password_lenght-1])):
            break
        
    return password


password = pass_gen()
pyperclip.copy(password)
print('your password is --> ', password)
print('your password is copied in clipboard')