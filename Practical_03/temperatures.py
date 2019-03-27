"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


# def main():
# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit : "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")
#
# def celsius():
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     return
# main()

def main():
    MENU = """C - Convert Celsius to Fahrenheit
            F - Convert Fahrenheit to Celsius
            Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != celsius_to_fahrenheit(celsius, fahrenheit):
        elif choice == "F":
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))

else:
print("Invalid option")
print(MENU)
choice = input(">>> ").upper()
print("Thank you.")


def celsius_to_fahrenheit(celsius, fahrenheit):
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    return


main()
