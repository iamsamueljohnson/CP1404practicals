import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBERS = 1
MAXIMUM_NUMBERS = 45


def main():
    user_input = int(input("Enter quick pick amount: "))
    while user_input < 0:
        print("Invalid input, must be > 0")
        user_input = int(input("Enter quick pick amount: "))
    for i in range(user_input):
        quick_pick = []
        for num in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBERS, MAXIMUM_NUMBERS)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBERS, MAXIMUM_NUMBERS)
            quick_pick.append(number)
            quick_pick.sort()
        # Looked at solution for final print
        print(" ".join("{:>2}".format(number) for number in quick_pick))


main()
