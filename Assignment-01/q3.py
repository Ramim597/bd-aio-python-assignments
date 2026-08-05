# Q3:  Ask the user to enter two integers and one float. Convert them all to floats
#      and print their average.

num1 = int(input("Enter a int (integers) number:"))
num2 = int(input("Enter another int (integers) number:"))
num3 = float(input("Enter a float number:"))

# convert integers to float
num1 = float(num1)
num2 = float(num2)

average = (num1 + num2 + num3) / 3
print(average)