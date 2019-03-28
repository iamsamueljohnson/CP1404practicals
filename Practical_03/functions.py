MIN_LENGTH = 5
MAX_LENGTH = 15


def main():
    get_password(MAX_LENGTH, MIN_LENGTH)


def get_password(max_length, min_length):
    password = input("Enter password")
    if len(password) < min_length or len(password) > max_length:
        password = input("Enter password")
    print(password)


main()
