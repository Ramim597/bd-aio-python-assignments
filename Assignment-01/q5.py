# Q5 : Evaluate and print the result of the following expression: x = 10 + 3 * 2 ** 2
#      Based on what you learnt in the previous explain why the output is what it is.

x = 10 + 3 * 2**2
print(x)


# (Python evaluates expressions according to operator precedence. First,
# the exponent operator (**) is evaluated, so 2 ** 2 = 4. Next, multiplication is
# performed: 3 * 4 = 12. Finally, addition is performed: 10 + 12 = 22. Therefore,
# the final value of x is 22.)
