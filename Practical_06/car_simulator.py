from Practical_06.car import Car


def main():
    car = []

    print("Let's drive!")
    name = input("Enter your car name: ")
    my_car = Car(name, 100)
    car.append(my_car)
    print("{self.name} fuel={self.fuel}, odo={self.odometer}".format(self=my_car))

    distance = int(input("How many km do you wish to drive?"))
    my_car.drive(distance)
    print("The car drove {}km.".format(distance))
    print("{self.name}, fuel={self.fuel}, odo={self.odometer}".format(self=my_car))


main()