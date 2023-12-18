import string
import secrets


def pass_gen():
    password_lenght = 12
    alphabet = string.ascii_letters + string.digits + ' $@!?~' 
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(password_lenght))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
                and any(c.isspace() for c in password)):
            break
        
    return password


password = pass_gen()
print(password)