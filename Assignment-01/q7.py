# Q7: Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print the temperature in Fahrenheit.
# Conversion Formula:
# Fahrenheit = (Celsius × (9 / 5)) + 32

temp_celsius = input("Enter temperature in Celsius:")
temp_float_celsius = float(temp_celsius)  # Convert string to flaot value
Fahrenheit = temp_float_celsius * (9 / 5) + 32
print(f"Temparature in Fahrenheit = {Fahrenheit}°F")
