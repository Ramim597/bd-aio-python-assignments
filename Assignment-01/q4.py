# Q4: The user enters a string containing a number (e.g.,"45" ). Convert it to:
#    1. an integer  2. a float  3. a string again  ~ Print all three values with their types

num = input("Enter a number:")
int_num = int(num)
float_num = float(num)
string_num = str(num)

# print theire value
print(f"Int num = {int_num} type of this = {type(int_num)}")
print(f"float num = {float_num} type of this = {type(float_num)}")
print(f"String = {string_num} type of this = {type(string_num)}")
