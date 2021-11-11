from car import  Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.drive()
car_1.stop()
print(car_1.model)

car_2.drive()
car_2.stop()
print(car_2.model)

Car.wheels = 2
car_1.wheels = 3

print(car_1.wheels)
print(car_2.wheels)

