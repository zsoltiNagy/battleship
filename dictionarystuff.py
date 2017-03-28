ship_dict = {
    "Carrier": [5, 1],
    "Battleship": [4, 1],
    "Cruiser": [3, 2],
    "Destroyer": [2, 3]
}

x = ship_dict["Cruiser"][0]

for ship in ship_dict:  # how to print the second value in every keys' list
    y = ship_dict[ship][1]
    print(y)

