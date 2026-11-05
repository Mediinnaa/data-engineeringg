name = input("Enter your name: ")
salary = float(input("Enter monthly salary (EUR): "))
rent = float(input("Enter rent (EUR): "))
food = float(input("Enter food expenses (EUR): "))
transport = float(input("Enter transport expenses (EUR): "))
internet = float(input("Enter internet expenses (EUR): "))
other = float(input("Enter other expenses (EUR): "))


total_expenses = rent + food + transport + internet + other
remaining_money = salary - total_expenses
spent_percentage = (total_expenses / salary) * 100
remaining_percentage = (remaining_money / salary) * 100


print("\n======= MONTHLY BUDGET =======")
print("Name:", name)
print(f"Monthly Income: {salary:.2f} EUR")
print(f"\nRent: {rent:.2f} EUR")
print(f"Food: {food:.2f} EUR")
print(f"Transport: {transport:.2f} EUR")
print(f"Internet: {internet:.2f} EUR")
print(f"Other Expenses: {other:.2f} EUR")
print(f"\nTotal Expenses: {total_expenses:.2f} EUR")
print(f"Remaining Money: {remaining_money:.2f} EUR")
print(f"Spent: {spent_percentage:.2f}%")
print(f"Remaining: {remaining_percentage:.2f}%")
print("==============================")
