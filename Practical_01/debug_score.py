score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")
