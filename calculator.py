print("Welcome to the tip calculator.")
bill = float(input("How big is your bill?\n"))

tip = float(input("What tip would you like to leave? (Enter as a whole number and not a percent)\n"))

party = int(input("How many people are in your party?\n"))

total = "{:.2f}".format(bill / party * (1+(tip/100)))

print(f"Everyone should pay this much: ${total}")
