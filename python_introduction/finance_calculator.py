# finance_calculator.py

income   = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses            # e.g. 1000.0

annual_rate   = 0.05
monthly_rate  = annual_rate / 12
months        = 12

# Future value of a 12‑month series of equal deposits with monthly compounding
projected_savings = monthly_savings * (((1 + monthly_rate) ** months - 1) / monthly_rate)

# Display results with no decimal places
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
