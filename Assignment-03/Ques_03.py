# Q3. Input two lists of integers from the user. Merge them into one list and sort the result.

# Example:
# list1 = [1, 2, 7]
# list2 = [2, 4, 5]

# Result:
# [1, 2, 2, 4, 5, 7]

try:
    list1 = list(map(int, input("Enter number: ").split()))
    list2 = list(map(int, input("Enter number: ").split()))
    result = list1 + list2
    result.sort()
    print(result)
except ValueError:
    print("Please enter numbers only!")
