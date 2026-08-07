# Q3: Given a list of integers compute the average of all numbers in the list.

nums = [5, 2, 3, 8]

total = 0
for num in nums:
    total += num

average = total / len(nums)
print(f"average = {average}")
