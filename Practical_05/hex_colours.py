HEX_COLOURS = {"Pastel magenta": "#f49ac2", "Mint green": "#98ff98", "Teal": "#008080", "Bittersweet": "#fe6f5e",
               "Battleship grey": "#848482", "Blue Gray": "#6699cc", "Blue violet": "#8a2be2",
               "Brilliant lavender": "#f4bbff", "Celeste": "#b2ffff", "Coffee": "#6f4e37"}
for colour in HEX_COLOURS:
    print(colour, "code:", HEX_COLOURS[colour])

colour = input("Enter colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "code:", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")
