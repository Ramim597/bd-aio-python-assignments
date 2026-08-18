# Q9: Create the following classes: Herbivore, Carnivore, Omnivore with some
# attributes & methods. Then create a class Bear that inherits from all the above
# classes to showcase how multiple inheritance works.


class Herbivore:
    founder_name = "Ramim"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Carnivore:
    NID = 112235535

    def __init__(self, nationality):
        self.nationality = nationality


class Omnivore:
    country = "Bangladesh"

    def __init__(self, capital):
        self.capital = capital


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name, age, nationality, capital):
        Herbivore.__init__(self, name, age)
        Carnivore.__init__(self, nationality)
        Omnivore.__init__(self, capital)


b1 = Bear("Ramim", 18, "Bangladesh", "Dhaka")
print(b1.name, b1.age, b1.nationality, b1.capital)
