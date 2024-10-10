# Ilori Ebenezer
# 10/10/24
# P2LAB1
# Let us price some apples today

print("What are you buying?")
name = input()
print("How many do you want")
number = int(input("Type a number"))
print("How much does each cost?")
price = float(input("Each costs: $"))
print("How much is sales tax")
salestax_price = float(input("equals: $"))
#Add expenses
Total_price = number * price + salestax_price
print("Total_price: $", format(Total_price,".2f"))


            
