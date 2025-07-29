# finance_calculator.py

# Prompt user for monthly income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Annual interest rate and monthly rate
annual_rate = 0.05
monthly_rate = annual_rate / 12
months = 12

# Compound interest formula for monthly deposits
projected_savings = monthly_savings * (((1 + monthly_rate) ** months - 1) / monthly_rate)

# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
