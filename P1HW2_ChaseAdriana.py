 # Adriana Chase
 # 6/15/2025
 # P1HW2
 # Create Budget

print("What is your budget: ", end = " ")
budget =  int(input())
print("What is your travel destination: ", end = " ")
destination =  input()
print("How much will you spend on gas: ", end = " ")
gas = int(input())
print("How much will you spend on accomodation: ", end = " ")
accomodation = int(input())
print("How much will you spend on food: ", end = " ")
food = int(input())
print("Add expenses", end = " ")
expenses = gas + accomodation + food
print("---------Travel Expenses---------")
print("Location: " + destination, end = " ")
print("Intital Budget: " + str(budget), end  = " ")

print("Fuel: " + str(gas))
print("accomodation:" + str(accomodation))
print("food: " + str(food))

print("Remaining Balance: ", + budget - expenses)
