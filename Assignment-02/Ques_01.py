# Q1: Write a program that takes salary as input.
# Using conditional statements, calculate the final tax rate based on these rules:

# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary = int(input("Enter your salary: "))
tax_rate = 0

if salary < 30_000:
    tax_rate = 5
elif 30_000 <= salary <= 70_000:
    tax_rate = 15
else:
    tax_rate = 25

print(f"According this salary = {salary} \ntax rate is = {tax_rate}%")
