 # Adriana Chase
 # 6/16/2025
 # P2LAB2
 # Dictionary Practice

my_dict={
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }

keys = my_dict.keys()

print(keys)

vehicle = input("Enter a vehicle to see its mpg: ")

mpg = my_dict[vehicle]

print("the " + str(vehicle) +  " gets " + str(mpg) + " mpg. ")

miles=float(input("How many miles will you drive the " + str(vehicle) + "? "))
            
gallons = miles/mpg

print(str(gallons) + " of gas are needed to drive the "  + str(vehicle) + " " + str(miles) + " miles.")
