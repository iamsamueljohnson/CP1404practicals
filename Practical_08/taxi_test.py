from Practical_08.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print("Current fare", my_taxi.get_fare())

    my_taxi.start_fare()
    my_taxi.add_fuel(40)
    my_taxi.drive(100)
    print(my_taxi)
    print("Current fare", my_taxi.get_fare())


main()
