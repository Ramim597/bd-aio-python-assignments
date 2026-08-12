# Q3: Create a class Student with private attributes _name, _roll_no, and _marks.

# Provide getter and setter methods with validation.
# - marks cannot be negative
# - roll number has to be between 1 & 100
# - name cannot be empty


class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # geter for name
    def get_name(self):
        return self.__name

    # seter for name
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("name cannot be empty")

    # geter for roo_num
    def get_roll_no(self):
        return self.__roll_no

    # seter for roll num
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("write roll number between 1 to 100")

    def get_marks(self):
        return self.__marks

    # seter for roll num
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("marks cannot be negative")


st1 = Student("hamim", 6, 98)
print(st1.get_name())
print(st1.get_roll_no())
print(st1.get_marks())
