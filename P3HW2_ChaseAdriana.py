 # Adriana Chase
 # 6/27/2025
 # P3HW2
 # Decision Structures


#################################Pseudocode**************************
##Assign a name variable to the user
##Assign a hours float variable to the user hours
##Assign a salary float variable
##Multiply salary * 1.5 to Assign a otsalary float variable
##Assign a otime to float variable to hours -40
##Calculate salary
##Add any otime salary
##Calculate regular salary
##Assign gross pay to value of otime salary at regular salary
##Display Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
###############################Pseudocode**************************


user = input("Enter Your Name: ")
hours = input("How many hours did you work: ")
salary = input("What is your salary: ")
otsalary = float(salary) * 1.5

if float(hours) > 40:
    otime = float(hours) - 40
else:
    otime = 0


otsalarytotal = float(otsalary) * float(otime)

salarytotal = float(hours) * float(salary)

finalsalary = float(otsalarytotal) + float(salarytotal)

###########################Display Data######################

print(user + " makes $" + str(salary) + " per hour. " + user + " worked for a total of " + str(hours) + " hours, of which " + str(otime) + " were overtime hours. " + "Overtime pay was $" + str(otsalarytotal) + ". Regular pay was $" +
      str(salarytotal) + ". " + user + " had a gross pay of $" + str(finalsalary) + ".")
