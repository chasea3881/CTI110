# Adriana Chase
# 7/6/2025
# P4HW2
# Calculate gross pay for multiple employees
#################################Pseudocode**************************
# Set up totals and employee count
# Ask for employee name (or type "Done" to quit)
# Create a while loop that runs until done is entered
# Get hours worked and pay rate
# OT = hours - 40 if hours > 40, otherwise 0
# OT rate = pay rate * 1.5
# OT pay = OT hours * OT rate
# Reg hours = 40 or however many they worked
# Reg pay = reg hours * pay rate
# Gross = reg + OT
# Add to totals and count
# Print results
# Ask for next name
# After loop:
# Print totals for OT, regular, gross, and employee count
###############################Pseudocode**************************
# Set all varaiables to zero
count = 0
total_ot_pay = 0
total_reg_pay = 0
total_gross_pay = 0
# Ask the user to enter an employee name or Done
name = input("Enter employee's name or \"Done\" to terminate: ")
# While the name is not "Done":
while name != "Done":
hours = float(input(f"How many hours did {name} work? "))
rate = float(input(f"What is {name}'s pay rate? "))
ot_rate = rate * 1.5
otime = hours - 40 if hours > 40 else 0
reg_hours = 40 if hours > 40 else hours
ot_pay = otime * ot_rate
reg_pay = reg_hours * rate
gross_pay = reg_pay + ot_pay
# Add this employee’s overtime pay, regular pay, and gross pay to the totals
total_ot_pay += ot_pay
total_reg_pay += reg_pay
total_gross_pay += gross_pay
# Add 1 to employee count
count += 1
# Display the employee name
print("\nEmployee name: ", name)
# Display the hours worked, pay rate, overtime hours, overtime pay,
# regular pay, and gross pay in requied format
print(f"\n{'Hours Worked':<13}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("-" * 75)
print(f"{hours:<13.1f}{rate:<10.2f}{otime:<10.1f}{ot_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<10.2f}")
# Ask the user to enter an employee name or Done
name = input("\nEnter employee's name or \"Done\" to terminate: ")
# After Loop
print("\nTotal number of employees entered:", count)
print("Total amount paid for overtime: $" + format(total_ot_pay, '.2f'))
print("Total amount paid for regular hours: $" + format(total_reg_pay, '.2f'))
print("Total amount paid in gross: $" + format(total_gross_pay, '.2f'))
