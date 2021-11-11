# Inheritance
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")


class Fish(Animal):
    def swim(self):
        print("Fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
rabbit.eat()
rabbit.slumber()
fish.swim()
hawk.fly()
hawk.eat()


# multi level inheritance
class Organism:
    alive = True

    def __init__(self):
        print("Organism constructor")


class Animal(Organism):
    def eat(self):
        print("This animal is eating")

    def __init__(self):
        super().__init__()
        print("Animal constructor")


class Dog(Animal):
    def bark(self):
        print("This dog is barking")

    def __init__(self):
        super().__init__()
        print("Dog constructor")


print()
dog = Dog()
dog.bark()
dog.eat()
print(dog.alive)
