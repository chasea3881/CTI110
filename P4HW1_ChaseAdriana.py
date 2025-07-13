# Adriana Chase
# 7/06/2025
# P4HW1
# Loop Score
# ###########################################################
################## Assignment PseudoCode ###################
###########################################################
# Ask the user how many scores they want to enter
# Ask for the first score
# If the score is not between 0 and 100, ask again
# Set total to the first score
# Set lowest to the first score
# Set count to 1
# Do a while loop
# While count is less than number of scores
# Subtract lowest from total
# Subtract 1 from number of scores
# Divide total by number of scores to get average
# Assign grade based on average
# Print lowest score
# Print average
# Print letter grade
###########################################################
num_scores = int(input("How many scores would you like to enter? "))
score_list = []
score = float(input("Enter Score: "))
while score < 0 or score > 100:
print("Invalid score. Score must be between 0 and 100.")
score = float(input("Enter a VALID Score: "))
score_list.append(score)
count = 1
while count < num_scores:
score = float(input("Enter score #" + str(count + 1) + ": "))
while score < 0 or score > 100:
print("Invalid score. Score must be between 0 and 100.")
score = float(input("Enter a VALID score #" + str(count + 1) + ": "))
score_list.append(score)
count = count + 1
lowest = min(score_list)
score_list.remove(lowest)
average = sum(score_list) / len(score_list)
print("----------------Results----------------")
print("Lowest Score :", lowest)
print("Modified List :", score_list)
print("Scores Average :", average)
# grade
if average >= 90:
grade = "A"
elif average >= 80:
grade = "B"
elif average >= 70:
grade = "C"
elif average >= 60:
grade = "D"
else:
grade = "F"
print("Grade :", grade)
print("---------------------------------------")
