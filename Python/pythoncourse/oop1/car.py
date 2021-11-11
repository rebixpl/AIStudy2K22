class Car:
    # Class Variables
    wheels = 4  # class variable is shared by all object instances of a class


    # Constructor
    def __init__(self, make, model, year, color):
        # Attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Methods
    def drive(self):
        print("{model} is driving!".format(model=self.model))

    def stop(self):
        print("{model} has stopped!".format(model=self.model))

