income = int(input("Enter your monthly income:"))  #Prompt the user for their monthly income
expenses = int(input("Enter your total monthly expenses:")) #Ask for their total monthly expenses
savings = income - expenses
print("Your monthly savings are", "$", savings,".")
rates = 0.05 #Assume a simple annual interest rate of 5%
#Calculating projected savings
projected_savings = int(savings * 12 + (savings * 12 * rates))
print("Projected savings after one year, with interest, is:", "$",projected_savings,".")