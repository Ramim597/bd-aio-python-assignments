# Q10. Ask the user for a string and print:
# - All unique characters
# - The count of unique characters

user_str = input("Enter a string: ").lower().replace(" ", "")

normal_set = set()
duplicate_ch = set()
for ch in user_str:
    if ch in normal_set:
        duplicate_ch.add(ch)
    else:
        normal_set.add(ch)
unique_ch = normal_set - duplicate_ch
print(f"unique characters = {unique_ch}")
print("The count of unique characters = ", len(unique_ch))
