total = 0
item_number = int(input("Please enter number of items: \n"))
while item_number <= 0:
    print("Invalid number of items.. Must be more than 0")
    item_number = int(input("Number of items: \n"))
for i in range(item_number):
    item_price = float(input("Please enter price of item: \n"))
    total += item_price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(item_number, total))
