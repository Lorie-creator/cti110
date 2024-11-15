# P3HW2
# Ilori
# 11/12/2024


# This program calculates an employee's working hours and overtime.


# Ask user to enter name of employee
# Ask user to enter number of hours an employee worked this week
# Ask user to enter employee's pay rate
# Evaluate if employee has worked overtime(more than 40 hours)
# If yes calculate the amount owed employee for overtime hours
# Calculate amount employee should be paid for regular hours worked.
# Display gross pay (total amount that should be paid to employee)



Employee_Name = input("Enter Employee's name:        ")
worked_ThisWeek = float(input("Enter number of hours worked: "))
Pay_Rate = float(input("Enter employee's pay rate:    "))
print("---------------------------------------")
print ("Employee name:    Mary Jane")

print ("Hours Worked   Pay Rate    Overtime   Overtime Pay  RegHour Pay  Gross Pay")

print("--------------------------------------------------------------------------------")


# Calculate amount owed to employee

Hours_Worked = 60
Pay_Rate = 17.5
RegHour_Worked = 40
Overtime = 20
RegHour_pay = Pay_Rate * RegHour_Worked
Overtimepay = 1.5 * Pay_Rate * Overtime
Grosspay = Overtimepay + RegHour_pay

print ( Hours_Worked,"\t" "\t",Pay_Rate, "\t" "\t", Overtime, "\t", Overtimepay,"\t", "\t",RegHour_pay,"\t", Grosspay,)  




