# CTI 110
# P2HW2
# Ilori
# 10/17/2024

# This program computes test grades


# Ask user to enter grade for module 1
# Ask user to enter grade for module 2
# Ask user to enter grade for module 3
# Ask user to enter grade for module 4
# Ask user to enter grade for module 5
# Ask user to enter grade for module 6


Module_1 = float(input("Enter grade for Module 1:     "))
Module_2 = int(input("Enter grade for Module 2:     "))
Module_3 = float(input("Enter grade for Module 3:     "))
Module_4 = int(input("Enter grade for Module 4:     "))
Module_5 = int(input("Enter grade for Module 5:     "))
Module_6 = int(input("Enter grade for Module 6:     "))

print("------------", "Results" "---------------")

Module_grades = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]
print("Lowest Grade:      ", min(Module_grades))
print("Highest Grade:     ", max(Module_grades))
print ("Sum of Grades:     ", sum(Module_grades))
average = sum(Module_grades) / len(Module_grades)
print("Average:           ",(round(average, 2)))






