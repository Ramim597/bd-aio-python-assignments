# Q9. Given a list, print all elements that appear more than once in the list.
# [Hint - use sets]

list_items = [4, 6, 7, 3, 6, 3, 6, 6, 9, 11]

seen = set()
duplicates = set()

for item in list_items:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(duplicates)
