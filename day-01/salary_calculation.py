employee_name = input("Enter your name: ")
basic_salary = float(input("Enter your salary: "))

house_rent = basic_salary * 0.40
medical_allowance = basic_salary * 0.10

total_salary = basic_salary + house_rent + medical_allowance

print("\nEmployee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("House Rent:", house_rent)
print("Medical Allowance:", medical_allowance)
print("Total Salary:", total_salary)