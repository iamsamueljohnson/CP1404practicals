def main():
    score = float(input("Enter score: "))
    print(calculate(score))


def calculate(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
