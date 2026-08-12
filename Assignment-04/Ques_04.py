# Q4: Create a class Shape with a method area().
# Create subclasses Circle, Rectangle, and Triangle
# that override the area() method.


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius**2


class Rectangle(Shape):
    def __init__(self, l, w):  # l = length & w = width
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


class Triangle(Shape):
    def __init__(self, b, h):  # b = base & h = height
        self.b = b
        self.h = h

    def area(self):
        return 1 / 2 * self.b * self.h


# circle area
c1 = Circle(3)
print(f"circle area = {c1.area()}")

# Rectangle area
r1 = Rectangle(3, 4)
print(f"Rectangle area = {r1.area()}")

# triangle area
tr1 = Triangle(9, 8)
print(f"Triangle area = {tr1.area()}")
