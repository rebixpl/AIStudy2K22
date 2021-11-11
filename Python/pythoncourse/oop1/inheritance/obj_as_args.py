# Objects as arguments
class Car:
    color = None


def changeColor(vehicle, color):
    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

changeColor(car_1, "red")
changeColor(car_2, "green")
changeColor(car_3, "blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)


# Duck Typing
# If it walks like a duck, and it quacks like a duck, then it must be a duck
class Duck:
    def walk(self):
        print("Duck is walking")

    def talk(self):
        print("Duck is talking")


class Chicken:
    def walk(self):
        print("Chicken is walking")

    def talk(self):
        print("Chicken is talking")


class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


print()
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)
