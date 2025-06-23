 # Adriana Chase
 # 6/22/2025
 # P2HW1
 # Format Budget

print("What is your budget: ", end = " ")
budget =  int(input())
print("What is your travel destination: ", end = " ")
destination =  input()
print("How much will you spend on gas: ", end = " ")
gas = int(input())
print("Approximately how much will you spend on accomodation/hotel: ", end = " ")
accomodation = int(input())
print("Last, how much do you need for food: ", end = " ")
food = int(input())
expenses = gas + accomodation + food
remaining = budget - expenses
print("---------Travel Expenses---------")
print("Location:           ",   destination)
print("Intital Budget:     ", f" ${budget}" )
print("Fuel:               ", f" ${gas}" )
print("Accomodation:       ", f" ${accomodation}" )
print("Food:               ", f" ${food}" )
print("---------------------------------")

print("Remaining Balance:", f"   ${remaining}" )
