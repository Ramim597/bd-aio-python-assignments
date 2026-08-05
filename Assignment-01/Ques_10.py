# Q10: Take a decimal number as input (like 45.78) and output its:

# • Integer part - 45
# • Fractional part - .78

num = float(input("Enter a num:"))

int_num = int(num)
fraction_num = num - int_num

print(f"Integer part - {int_num}")
print(
    f"Fractional part - {fraction_num:.2f}"
)  # :.2f tells Python to display the number with exactly 2 digits after the decimal point.
# convert .780000000009 to .78
