def main():
    MIN_LENGTH = 5
    MAX_LENGTH = 15
    get_password(MAX_LENGTH, MIN_LENGTH)


def get_password(MAX_LENGTH, MIN_LENGTH):
    password = input("Enter password")
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        password = input("Enter password")
    print(password)


main()
