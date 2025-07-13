# Adriana Chase
# 7/10/2025
# P5Lab
# Self Checkout


import random

def give_change(change):
    convertedToCents = int(round(change * 100))
    dollars = convertedToCents // 100
    remainder = convertedToCents % 100
    quarters = remainder // 25
    remainder = remainder % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    pennies = remainder % 5

    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(f"{pennies} Pennies")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed}")
    cash_given = float(input("Enter the amount of money you are putting into the machine: $"))
    
    if cash_given < total_owed:
        print("That's not enough money. Transaction cancelled.")
        return

    change = round(cash_given - total_owed, 2)
    print(f"Change owed: ${change}")
    give_change(change)

main()
