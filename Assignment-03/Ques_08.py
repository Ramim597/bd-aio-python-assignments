# Q8. Write a program to check whether two lists share no common elements.

# Example 1:
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# Example 2:
# list1 = [1, 2, 3]
# list2 = [3, 4]

# Hint: Use sets


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8]

set_list1 = set(list1)
set_list2 = set(list2)

if set_list1 & set_list2 == set():
    print("There is no common value")
else:
    print("There is common value")
