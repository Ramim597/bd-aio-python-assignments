# Q7: Create a class Person that allows the constructor to work with:
# - name only
# - name + age
# - name + age + address
#
# As direct constructor overloading (multiple constructors) are not allowed,
# use default parameters to simulate constructor overloading.


class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address


p1 = Person("ramim", 12)
print(p1.name, p1.age, p1.address)
