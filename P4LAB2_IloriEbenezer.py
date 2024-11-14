# CTI 110
# P4LAB2
# Ilori
# 11/14/24
"""
print("test program")
count = 1
while count <= 5:
    print("count is", count)
    count += 1
print("done")

for number in range (1,6):
    print(number)
print("done")

# input validation
num = int(input("Type a number from 1 to 3:"))
while num < 1 or num > 3:
    print("please try again")
    num = int(input("Type a number from 1 to 3:"))
print("you entered:", num)
"""

# P4LAB2 - Times Tables
# CTI 110
# P4LAB2
# Ilori
# 11/14/24
# ask for a number that is 0 or higher
# then display the times table for that number
# from times 1 to times 12

def times_table():
    num = int(input("Enter an interger:"))
    while (num < 0):
        print("No negative number please.")
        num = int(input("Enter an interger: "))
    print("You entered", num)
    # finally, do the times table
    for num2 in range (1,13):
        answer = num * num2
        print (num, "*",num2,"=",answer)

def main():
    times_table()
    again = input("Do you want to run again? ")
    while (again == "yes"):
        times_table()
        again = input("Do you want to run again? ")
    print("Goodbye!")

# start program
main()
                    
