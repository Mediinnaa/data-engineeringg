name = input("Enter freelancer name: ")
hours = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate (EUR): "))
bonus = float(input("Enter monthly bonus (EUR): "))
tax_percentage = float(input("Enter tax percentage (%): "))


base_income = hours * hourly_rate
gross_income = base_income + bonus
tax_amount = gross_income * tax_percentage / 100
net_income = gross_income - tax_amount


print("\n====== FREELANCER REPORT ======")
print("Freelancer:", name)
print("Hours Worked:", hours)
print(f"Hourly Rate: {hourly_rate:.2f} EUR")
print(f"\nBase Income: {base_income:.2f} EUR")
print(f"Bonus: {bonus:.2f} EUR")
print(f"Gross Income: {gross_income:.2f} EUR")
print(f"Tax ({tax_percentage}%): {tax_amount:.2f} EUR")
print(f"\nNET INCOME: {net_income:.2f} EUR")
print("===============================")



