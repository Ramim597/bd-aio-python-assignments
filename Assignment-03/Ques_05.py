# Q5. Create a dictionary where:
#     - Keys = student names
#     - Values = marks (integer)

# Write a menu-based program where user presses a key ('A', 'B', 'C', 'D')
# depending on the operation they want to perform on the dictionary:

# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks


# students = {"Ramim": 85, "Tanu": 72, "Suborna": 91, "Nadia": 78, "Hamim": 88}
# students.update({"Saim"})
# print(students)


import keyboard

if keyboard.is_pressed("a"):
    print("A pressed!")
