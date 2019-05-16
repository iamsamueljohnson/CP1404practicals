from Practical_08.unrealiable_car import UnreliableCar


def main():
    test_good = UnreliableCar("Good", 100, 100)
    test_bad = UnreliableCar("Bad", 100, 4)

    for i in range(1, 10):
        print("Attempting to drive {}km:\n".format(i))
        print("{} drove {}km".format(test_good.name, test_good.drive(i)))
        print("Attempting to drive {}km:\n".format(i))
        print("{} drove {}km".format(test_bad.name, test_bad.drive(i)))


main()
