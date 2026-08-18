# Q1. Create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

with open("names.txt", "w") as f:
    for i in range(1, 6):
        names = input(f"Enter name {i}: ")
        f.write(f"{names}\n")

with open("names.txt", "r") as f:
    content = f.read()
    print(content)
