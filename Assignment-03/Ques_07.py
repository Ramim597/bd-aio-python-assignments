# Q7 : Write a program that takes a string from the user and prints the number of spaces in the string.

user_string = input("Enter a string: ")

original_length = len(user_string)
without_spaces = user_string.replace(" ", "")

space_num = original_length - len(without_spaces)

print(f"The space number = {space_num}")
