from Practical_06.car import Car


def main():
    car = []
    minimum_length = 1
    print("Let's drive!")
    name = input("Enter your car name: ")
    while len(name) < minimum_length:
        print("Must have a name!")
        name = input("Enter your car name: ")
    my_car = Car(name, 100)
    car.append(my_car)
    print("{self.name} fuel={self.fuel}, odo={self.odometer}".format(self=my_car))
    menu = "Menu:\nd) Drive\nr) Refuel\nq) Quit"
    print(menu)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "D":
            distance = int(input("How many km do you wish to drive?"))
            my_car.drive(distance)
            print("The car drove {}km.".format(distance))
            print("{self.name}, fuel={self.fuel}, odo={self.odometer}".format(self=my_car))

            if my_car.fuel < distance:
                print("The car drove {self.fuel} and ran out of fuel.".format(self=my_car))

            print(menu)
            choice = input("Enter your choice: ").upper()

        else:
            print("Invalid choice")
            print(menu)
            choice = input("Enter your choice: ").upper()
    print("Thank you")


main()