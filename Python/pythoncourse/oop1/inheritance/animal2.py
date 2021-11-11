from abc import ABC, abstractmethod


# Multiple Inheritance
class Prey:
    def flee(self):
        print("This animal flees")
        return self


class Predator:
    def hunt(self):
        print("This animal is hunting")
        return self

    def prepare_to_attack(self):
        print("Walking towards prey")
        return self


class Fish(Prey, Predator):
    # Method Overriding
    def hunt(self):
        print("This fish is hunting")
        return self


fish = Fish()
fish.flee()
fish.hunt()

# Method Chaining
# Method must return self for this to work
print()
fish.prepare_to_attack() \
    .hunt() \
    .flee() \
    .prepare_to_attack() \
    .hunt() \
    .flee()


# Super Function
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())  # 9
print(cube.volume())  # 27


# Abstract  Classes
# from abc import ABC, abstractmethod
# Prevent user from creating an object of that class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("Car has stopped")


class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("Motorcycle has stopped")


# vehicle = Vehicle()  # Error =>  Can't instantiate abstract class Vehicle with abstract methods go, stop
motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()
