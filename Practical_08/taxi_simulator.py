from Practical_08.taxi import Taxi
from Practical_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None

    print("Let's Drive")
    print(MENU)

    user_menu = input(">>> ").lower()
    while user_menu != "q":
        if user_menu == "c":
            print("Taxis available: ")
            view_taxis(taxis)
            user_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[user_taxi]

        elif user_menu == "d":
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            distance_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, distance_cost))
            bill += distance_cost

        else:
            print("Invalid option")
        print("Current bill: ${:.2f}".format(bill))
        print(MENU)
        user_menu = input(">>> ").lower()
    print("Taxis are now:")
    view_taxis(taxis)


def view_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
