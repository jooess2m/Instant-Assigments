team_members = int(input("Enter number of team members: "))
months = int(input("Enter project duration in months: "))
monthly_salary = float(input("Enter monthly salary: "))
cloud_cost = float(input("Enter total cloud cost: "))

salary_cost = team_members * months * monthly_salary
subtotal = salary_cost + cloud_cost
vat = subtotal * 0.14
total = subtotal + vat

print("\n========== PROJECT COST ==========")
print(f"Salary cost: {salary_cost:,.2f}")
print(f"Subtotal:    {subtotal:,.2f}")
print(f"VAT (14%):   {vat:,.2f}")
print(f"Total:       {total:,.2f}")