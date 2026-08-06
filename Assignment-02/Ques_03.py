# Q3. Write a function that prints the digits of a number, `n`.
#    For example:
#    n = 312
#    There are 3 digits in it: 3, 1, and 2, and we need to print them.
#    Hint:
# -  The rightmost digit of a number `n` is `n % 10`.
# -  To remove the rightmost digit from a number, we can do `n = n // 10`.

nums = input("Enter a number: ") # it will get a number as a string


def print_digits(nums):

    for n in nums:
        print(n)


print_digits(nums)
