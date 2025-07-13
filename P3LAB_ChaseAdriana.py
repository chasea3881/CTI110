# Adriana Chase
# 6/27/2025
# P3Lab
# Calculate Coins
howMuch = float(input("Enter the amount of money as a float: "))
convertedToCents = int(round(howMuch * 100))
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
