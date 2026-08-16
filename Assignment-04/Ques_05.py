# Q5: Create a base class Vehicle with attributes like brand and model.
# Create two subclasses Car and Bike that add extra attributes:
# seats (in Car) and engine_cc (in Bike).


class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand


class Car(Vehicle):
    def __init__(self, seats, model, brand):
        super().__init__(model, brand)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, engine_cc, model, brand):
        super().__init__(model, brand)
        self.engine_cc = engine_cc


c1 = Car(6, "bmwi5", "BMW")
print(c1.seats, c1.model, c1.brand)
bike1 = Bike(155, "R15", "Yamaha")
print(bike1.brand, bike1.model, bike1.engine_cc)
