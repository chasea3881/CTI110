 # Adriana Chase
 # 6/16/2025
 # P2HW2
 # List Practice
 
###########################################################
##################Assignment PseudoCode####################
###########################################################

#This is a python a program to store module grades
 
#1.  Create a List to store Module Grades
#2.  Prompt the user to enter the grade of Module 1
#3.  Prompt the user to enter the grade of Module 2
#4.  Prompt the user to enter the grade of Module 3
#5.  Prompt the user to enter the grade of Module 4
#6.  Prompt the user to enter the grade of Module 5
#7.  Prompt the user to enter the grade  of Module 6
#8.  Identify Results Section
#9.  Display Lowest Grade from list
#10. Display Highest Grade from list
#11. Display Sum of Grades from list
#12. Display Average of Grades list
#13. Close Results Section list
##########################################################

grades=[]

grade1 = float(input("Enter grade for Module 1: "))
grades.append(grade1)

grade2 = float(input("Enter grade for Module 2: "))
grades.append(grade2)

grade3 = float(input("Enter grade for Module 3: "))
grades.append(grade3)

grade4 = float(input("Enter grade for Module 4: "))
grades.append(grade4)

grade5 = float(input("Enter grade for Module 5: "))
grades.append(grade5)

grade6 = float(input("Enter grade for Module 6: "))
grades.append(grade6)

print("*********************Results********************")

low = min(grades)
high = max(grades)
total = sum(grades)
average = total / 6

print("Lowest Grade:     ", low)
print("Highest Grade:    ", high)
print("Sum of Grades:    ", total)
print("Average Grade:    ", average)

print("***************************************************")
 
