# Q2. Write a function that takes two integers `a` and `b` and prints all even numbers
#    between them (inclusive).

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))


def even_nums(a, b):
    print(f"even numbers from {a} to {b}:")
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)


even_nums(a, b)
