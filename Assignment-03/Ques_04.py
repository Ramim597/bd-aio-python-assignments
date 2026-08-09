# Q4. Given a tuple of integers, create:
# - A tuple of all even numbers
# - A tuple of all odd numbers

nums = (12, 7, 25, 4, 18, 33, 10, 9, 42, 15)
even = ()
odd = ()
for num in nums:
    if num % 2 == 0:
        even += (num,)
    else:
        odd += (num,)

print("Even numbers:", even)
print("Odd numbers:", odd)
