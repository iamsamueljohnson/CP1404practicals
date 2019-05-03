from Practical_06.car import Car
MENU = "Menu:\nd) Drive\nr) Refuel\nq) Quit"

def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    while name == "":
        print("Must have a name!")
        name = input("Enter your car name: ")
    my_car = Car(name, 100)
    print("{self.name}, fuel={self.fuel}, odo={self.odometer}".format(self=my_car))

    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "D":
            distance = int(input("How many km do you wish to drive?"))
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive?"))
            distance_driven = my_car.drive(distance)
            if my_car.fuel == 0:
                print("The car drove {}km and ran out of fuel.".format(distance_driven))
            else:
                print("The car drove {}km.".format(distance_driven))
        elif choice == "R":
            refuel = int(input("How many units of fuel do you want to add to the car?"))
            while refuel < 0:
                print("Fuel amount must be >= 0")
                refuel = int(input("How many units of fuel do you want to add to the car?"))
            my_car.add_fuel(refuel)
            print("Added {self.fuel} units of fuel.".format(self=my_car))
        else:
            print("Invalid choice")
        print("{self.name}, fuel={self.fuel}, odo={self.odometer}".format(self=my_car))
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Good bye {}'s driver.".format(name))


main()
