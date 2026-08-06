# Q5: Write a function to return the sum of digits of a number, n.


# def count_digits(n):

#     sum = 0

#     while n > 0:
#         sum += n
#         n = n // 10
#     return sum


# n = int(input("Enter a number: "))
# print(count_digits(n))


def sum_of_digits(n):
    total = 0
    
    while n > 0:
        digit = n % 10  # to get the last digit.
        total += digit
        n = n // 10  # to remove the last digit.

    return total

n = int(input("Enter a number: "))
print(f"Total sum of digits = {sum_of_digits(n)}")
