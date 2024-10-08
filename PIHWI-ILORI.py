# CTI 110
# P1HW1 - MATH
# Ilori
# 10/3/24

print("P1HW1")

#declare variables 

base_interger = 0
base_exponent = 0
base_toatlexponent= 0
base_starting = 0
base_add = 0
base_subtract = 0
base_totalmath = 0

#enter first question
print ("-"*5, "Calculating Exponents", "-" * 5)

base_interger = int(input("Enteran interger as a base value: ") )

base_exponent = int(input("Enter an interger as the exponent") )

base_totalexponent= base_interger**base_exponent

print(base_interger, "raised to the power of", base_exponent, "is", base_totalexponent)

print("-----", "Addition and Subtraction", "-----")

base_starting = int(input("Enter a starting interger: ") )

base_add = int(input("Enter an interger to add: "))

base_subtract = int(input("Enteran interger to subtract: ") )

base_totalmath = base_starting + base_add - base_subtract

print(base_starting, "+", base_add, "-", base_subtract, "is equal to", base_totalmath)