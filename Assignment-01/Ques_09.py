# Q9: Ask the user for:
# Principal (P), Rate (R), Time (T).
# Convert all to float and compute simple interest.

# Formula:
# SI = (P × R × T) / 100

principal = float(input("Enter the principal:"))  # eg: 40000
rate = float(input("Enter rate:"))  # eg: 12%
time = float(input("Enter Time(year):"))  # 5 year

si = (principal * rate * time) / 100

print("Simple Interest =", si)
