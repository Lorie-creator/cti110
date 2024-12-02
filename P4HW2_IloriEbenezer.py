# P4HW2
# Ilori
# 11/20/2024


# This program calculates an employee's working hours and overtime.


# Ask user to enter name of employee
# Ask user to enter number of hours an employee worked this week
# Ask user to enter employee's pay rate
# Evaluate if employee has worked overtime(more than 40 hours)
# If yes calculate the amount owed employee for overtime hours
# Calculate amount employee should be paid for regular hours worked.
# Display gross pay (total amount that should be paid to employee)



Employee1_Name = input("Enter Employee's name:        ")
worked_ThisWeek = float(input("Enter number of hours worked: "))
Pay_Rate = float(input("Enter employee's pay rate:    "))
print("---------------------------------------")
print ("Employee name:    Mary Jane")

print ("Hours Worked   Pay Rate    Overtime   Overtime Pay  RegHour Pay  Gross Pay")

print("--------------------------------------------------------------------------------")


# Calculate amount owed to employee1

Employee1_HoursWorked = 60
Employee1_PayRate = 17.5
Employee1_RegHour = 40
Employee1_Overtime = 20
Employee1_RegHourPay = Employee1_PayRate * Employee1_RegHour
Employee1_Overtimepay = 1.5 * Employee1_PayRate * Employee1_Overtime
Employee1_Grosspay = Employee1_Overtimepay + Employee1_RegHourPay

print ( Employee1_HoursWorked,"\t" "\t",Employee1_PayRate, "\t" "\t", Employee1_Overtime, "\t", Employee1_Overtimepay,"\t", "\t",Employee1_RegHourPay,"\t", Employee1_Grosspay)

# Imput data for second employee

Employee2_Name = input("Enter Employee's name:        ")
worked_ThisWeek = float(input("Enter number of hours worked: "))
Pay_Rate = float(input("Enter employee's pay rate:    "))
print("---------------------------------------")
print ("Employee name:    Peter Piper")

print ("Hours Worked   Pay Rate    Overtime   Overtime Pay  RegHour Pay  Gross Pay")

print("--------------------------------------------------------------------------------")


# Calculate amount owed to employee2

Employee2_HoursWorked = 45
Employee2_PayRate = 18.5
Employee2_RegHour = 40
Employee2_Overtime = 5
Employee2_RegHourPay = Employee2_PayRate * Employee2_RegHour
Employee2_Overtimepay = 1.5 * Employee2_PayRate * Employee2_Overtime
Employee2_Grosspay = Employee2_Overtimepay + Employee2_RegHourPay

print ( Employee2_HoursWorked,"\t" "\t",Employee2_PayRate, "\t" "\t", Employee2_Overtime, "\t", Employee2_Overtimepay, "\t",Employee2_RegHourPay,"\t", Employee2_Grosspay)


print("Total number of employees enetered:   2")
#Add amount paid for overtime
Total_Overtime = Employee1_Overtimepay + Employee2_Overtimepay
print("Total amount paid for overtime:       $", format(Total_Overtime,".2f"))
# Add amount paid for regular hours
Total_RegHour = Employee1_RegHourPay + Employee2_RegHourPay
print("Total amount paid for regular hours:  $", format(Total_RegHour,".2f"))
# Add amount paid in gross
Total_Gross = Employee1_Grosspay + Employee2_Grosspay
print("Total amount paid in gross:           $", format(Total_Gross,".2f"))
