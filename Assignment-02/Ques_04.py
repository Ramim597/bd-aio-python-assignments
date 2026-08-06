# Q4: Write a function to return the count of the number of digits in a number, n.


def count_digits(n):

    count = 0

    while n > 0:
        count += 1
        n = n // 10
    return count


n = int(input("Enter a number: "))
print(count_digits(n))
