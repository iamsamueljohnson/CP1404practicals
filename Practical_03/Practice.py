MIN_LENGTH = 5
MAX_LENGTH = 15

password = input("Enter password")
if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
    password = input("Enter password")
print(len(password) * '*')
