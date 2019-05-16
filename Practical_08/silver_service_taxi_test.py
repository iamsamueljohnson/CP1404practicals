from Practical_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Silver Service Taxi", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
