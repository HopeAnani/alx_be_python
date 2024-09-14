monthly_income = int (input('Enter your montly income: '))
monthly_total_expense = int (input('Enter you total monthly expenses: '))

monthly_saving = monthly_income - monthly_total_expense

projected_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f'Your monthly savings are: ${monthly_saving}.')
print(f'Projected savings after one year, with interest, is: ${projected_saving}.')