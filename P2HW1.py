# CTI 110
# P2HW1 - Budget
# Ilori
# 10/8/24

# This program starts a travel budget

# Ask user to enter their travel location
# Ask user to enter their initial budget
# Ask user for the amount they will spend on gas
# Ask user for the amount they will spend on accommodation
# Ask user for the amount they will spend on food
# Add expenses
# subtract expenses from initial budget
# Display results

print("------------", "Travel Expenses" "------------")
# Ask user to enter their travel location
Location = input("Location:")
# Ask user to enter their initial budget
Initial_Budget =float(input("Initial Budget:      $"))
# Ask user for the amount they will spend on gas
Budget_Gas = float(input("Fuel:                $"))
# Ask user for the amount they will spend on accommodation
Budget_Accommodation = float(input("Accommodation:       $"))
# Ask user for the amount they will spend on food
Budget_Food = float(input("Food:                $"))
print("----------------------------------------")
# subtract expenses from initial budget
Remaining_Balance = Initial_Budget - Budget_Gas - Budget_Accommodation - Budget_Food
print("Remaining Balance:   $", format(Remaining_Balance, ".2f"))
