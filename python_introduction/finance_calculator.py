monthly_income = int(input("Enter your monthly income: "))  # Prompt the user for their monthly income
monthly_expenses = int(input("Enter your total monthly expenses: "))  # Ask for their total monthly expenses

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}.")

annual_interest_rate = 0.05  # Assume a simple annual interest rate of 5%
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate))  # Calculating projected savings

print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
