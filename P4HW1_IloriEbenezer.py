# CTI 110
# P4HW1
# Ilori
# 11/22/2024

# This program computes test grades


# Ask user how many scores they want to enter
# Create a loop to collect the number of scores user wants to enter
# Evaluate if the score is valid
# Ask user to enter grade for module 4
# Ask user to enter grade for module 5
# Ask user to enter grade for module 6


Score_total = int(input("How many scores do you want to enter?     "))
Score_1 = int(input("Enter score #1:     "))
while Score_1 <=0:
    print("Must be a positive number.")                    
Score_2 = int(input("Enter score #2:     "))
while Score_total <=0:
    print("Must be a positive number.")
Score_3 = int(input("Enter score #3:     "))
while Score_total <=0:
    print("Must be a positive number.")
Score_4 = int(input("Enter score #4:     "))
while Score_total <=0:
    print("Must be a positive number.")
Score_5 = int(input("Enter score #5:     "))


    
    


print("------------", "Results" "---------------")

Score_grades = [Score_1, Score_2, Score_3, Score_4, Score_5]
print("Lowest Grade  :  ", min(Score_grades))
Modified_List = [Score_1, Score_2, Score_3, Score_5]
print("Modified List :  ", list(Modified_List))
average = sum(Modified_List) / len(Modified_List)
print("Scores Average:  ",(round(average, 2)))
if average >= 90:
    Grade = "A"
elif average >= 80:
    Grade = "B"
elif average >= 70:
    Grade = "C"
elif average >= 60:
    Grade = "D"
elif average >= 50:
    Grade = "F"

print("Grade         :  ", Grade)
