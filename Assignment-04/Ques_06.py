# Q6: Create an abstract class Employee with an abstract method
# calculate_salary().
# Create subclasses Intern, FullTimeEmployee, and ContractEmployee
# that implement the method differently.

from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        return 10_000


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 35_000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 23_000


i1 = Intern()
print(i1.calculate_salary())

f1 = FullTimeEmployee()
print(f1.calculate_salary())

c1 = ContractEmployee()
print(c1.calculate_salary())
