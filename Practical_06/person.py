class Person:
    def __init__(self, full_name="", age=0):
        people_list = []
        self.full_name = full_name
        self.age = age

    def __str__(self):
        return "{} {}".format(self.full_name, self.age)


MENU = "q) Quit  a) Add  l) List"


def main():
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "A":
            full_name = input("Enter full name: ")
            age = int(input("Enter age: "))
            add_person = Person(full_name, age)
            print("You added '{}' to the list".format(add_person))
        elif choice == "L":
                print("{self.full_name} {self.age}".format(self=add_person))
            print(Person)
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Goodbye!")


main()
