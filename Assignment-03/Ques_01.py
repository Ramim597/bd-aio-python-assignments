# Q1. Ask the user for a string and check whether it is a palindrome or not.

# A palindrome is a string which is same when we read it forward & backward.
# Eg - "madam", "racecar" etc.

# Hint:
# A palindrome string is equal to the reversed version of the string.

user_str = input("Enter a string:")
reversed_str = user_str[::-1]
if user_str == reversed_str:
    print("Palindrome")
else:
    print("NOT Palindrome")
