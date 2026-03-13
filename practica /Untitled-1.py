coffee = 4000
tea = 3500
juice = 5000

print("Choose a drink: coffee, tea, juice")

drink = input("What drink do you want? ")
quantity = int(input("How many drinks do you want? "))

if drink == "coffee":
    total = coffee * quantity
elif drink == "tea":
    total = tea * quantity
elif drink == "juice":
    total = juice * quantity

print("Total to pay:", total)
