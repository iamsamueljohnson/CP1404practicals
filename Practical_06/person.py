class Person:
    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.age)

    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        print(full_name)

def main():
    person = []
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age"))


main()