# Q10: Let's create a "Number Guessing Game".

# Given a secret number (already decided by you),
# write a program that asks the user to guess it
# and prints:

# "Too high" if the guess is above the number.

# "Too low" if the guess is below the number.

# "Correct!" if the guess matches.

num = 42
guess = int(input("Guess the number: "))

if guess > num:
    print("Too high")
elif guess < num:
    print("Too low")
else:
    print("Correct!")
