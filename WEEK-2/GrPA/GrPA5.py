password = input()
if 8 <= len(password) <= 32:
    if password[0].isupper() or password[0].islower():
        if '/' not in password and '\\' not in password and '=' not in password and "'" not in password and '"' not in password and ' ' not in password:
            print('True')
        else:
            print('False')
    else:
        print('False')
else:
    print('False')