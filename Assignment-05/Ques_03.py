# Q3. Create a program that:
# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list with only numbers greater than 15
# 3. Prints the new list

nums = [5, 10, 15, 20, 25]

greter_than_15 = [i for i in nums if i > 15]
print(greter_than_15)
