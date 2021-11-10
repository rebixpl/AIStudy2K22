import math
import time
import random
import os
import shutil
import messages as msg

print("JD")

# String
first_name = "John"
last_name = "Fuck"
full_name = first_name + " " + last_name
print(type(full_name))  # <class 'str'>
print("Hello, " + full_name)  # Hello, John Fuck

# Int
age = 24
age += 2
print("Your age is: " + str(age))  # Your age is: 26

# Float
height = 180.5
print("Your height is: " + str(height))

# Multiple assignment
name, age, attractive = "Abdul", 46, False

print(name)
print(age)

aaa = bbb = ccc = 30

print(aaa)
print(bbb)
print(ccc)

# Strings
name = "Grzegorz Bryla"
print(len(name))  # 14
print(name.find("a"))  # 13
print(name.capitalize())  # Grzegorz bryla
print(name.upper())  # GRZEGORZ BRYLA
print(name.lower())  # grzegorz bryla
print(name.isdigit())  # False
print(name.isalpha())  # False because of space
print(name.replace("G", "B"))  # Brzegorz Bryla
print(name.split(" "))  # ['Grzegorz', 'Bryla']
print(name.count('Bryla'))  # 1
print(name.startswith("Grz"))  # True
print(name.endswith("ryla"))  # True
print(name.find("ryla"))  # 10
print(name * 3)  # Grzegorz BrylaGrzegorz BrylaGrzegorz Bryla

# User Input
# name = input("What's ur name?")
# print("Hello, " + name)

# height = float(input("How long is ur pp?"))
# print("Your pp is " + str(height) + " long.")

# math
# import math
pi = 3.14

print(round(pi))  # 3
print(math.ceil(pi))  # 4
print(math.floor(pi))  # 3
print(abs(-pi))  # 3.14
print(pow(pi, 2))  # 9.8596
print(math.sqrt(420))  # 20.493901531919196
print(max(2, 3, 4, 5))  # 5
print(min(2, 3, 4, 5))  # 2

# String Slicing
name = "Grzegorz Bryla"
first_name = name[0:5]
last_name = name[6:]
print(first_name + " " + last_name)  # Grzegorz Bryla
reversed_name = name[::-1]
print(reversed_name)  # alyrB zrogezrG

# ------------------------------------------------------
website = "http://google.com"
website2 = "http://cornhub.com"

slice = slice(7, -4)
print(website[slice])  # google
print(website2[slice])  # cornhub

# Statements
age = 24
if age == 100:
    print("You are 100 years old")
elif age >= 18:
    print("You are old enough to vote!")
elif age < 0:
    print("You are not born yet.")
else:
    print("Sorry, you are too young to vote.")

# logical operators
# temp = int(input("What's the temperature outside?"))
temp = 34

if not (temp >= 0 and temp <= 30):
    print("the temperature is bad today!")
    print("Stay inside!")
elif not (temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("go outside")

# While Loops
# name = None
# while not name:
#     name = input("Enter your name: ")

# print("Hello " + name)

# for loops
for i in range(50, 100 + 1, 10):
    print(i)

for i in "Pizda":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(0.100)
print("Happy New Year")

# nested loops
rows = 4
columns = 6
symbol = '#'

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# Loop Control Statements
while True:
    # name = input("give me your name: ")
    name = "Jake"
    if name != "":
        break

phone_number = "123-435-645"
pNumber = ""
for i in phone_number:
    if i == "-":
        continue
    pNumber += i

print(pNumber)  # 123435645

for i in range(1, 21):
    if i == 13:
        pass  # when pass is executed nothing happens
    else:
        print(i)

# Lists
food = ["pizza", "hamburger", "nigga", "cat", "piztah"]

print(food[3])  # cat
food[2] = "cebularz"
print(food[2])

for x in food:
    print(x)

food.append("Ice Cream")
food.remove("cat")
food.pop()  # removes last element
food.insert(0, "cake")
food.sort()

print()
for x in food:
    print(x)

food.clear()

# 2D Lists
drinks = ["coffe", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food)
print(food[0])  # drinks list
print(food[0][1])  # soda

# Tuples
# Collection which is ORDERED and UNCHANGEABLE used to group related data
student = ("Patrick", 23, "male")
print(student.count("male"))  # 1
print(student.index("male"))  # 2

for x in student:
    print(x)

if "Patrick" in student:
    print("Patrick is here!")

# Sets
# Set is an unordered, unindexed collection, and cannot contain duplicates
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

print()
for x in utensils:
    print(x)

utensils.add("napkin")
utensils.remove("fork")

# adding one set ot another with update() method
utensils.update(dishes)
print()
for x in utensils:
    print(x)

print(utensils.difference(dishes))  # {'spoon', 'napkin'}
print("DDD")
print(utensils.intersection(dishes))  # prints whatever they have in common => {'plate', 'knife', 'cup', 'bowl'}

dinner_table = utensils.union(dishes)  # combines two sets and returns it to a new variable

print(dinner_table)

utensils.clear()

# Dictionaries
# Something like a map => changeable, unordered collection of key:value pairs
capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow",
}

capitals.update({"Poland": "Warsaw"})
capitals.pop("China")  # removes a pair

print()
# print(capitals['RPA'])  # Gives and Error
print(capitals.get("Germany"))  # Much safer way, if key:value pair doesn't exist, returns None
print(capitals.keys())
print(capitals.values())
print(capitals.items())  # prints entire dictionary

print()
for key, value in capitals.items():
    print(key + " : " + value)

capitals.clear()


# Functions
def hello(first_name, last_name, age, num1, num2):
    print("Hello " + first_name + " " + last_name + "!")
    print("You are " + str(age))
    return num1 * num2


print()
my_name = "James"
number2 = hello(my_name, "Baryła", 23, 5, 4)

print(number2)


# keyword arguments
def hello2(first, middle, last):
    print("Hello " + first + middle + last)


hello2(last="JDL", middle="JDM", first="JDF")


# *args
# parameter that will pack all arguments into a tuple
def add(*args):
    sum = 0
    stuff = list(args)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))


# **kwargs
# parameter that will pack all arguments into a dictionary
def hello3(**names):
    print("hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")


hello3(title="Mr.", first="John", middle="Fuck", last="Code")

# String format() method
animal = "cow"
item = "moon"

print()
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(item, animal))  # Positional Argument
print("The {animal} jumped over the {item}".format(item="moon", animal="cow"))  # Keyword Argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

pi2 = 3.14159
number = 1000000

print("pi is: {:.2f}".format(pi2))  # pi is: 3.14
print("The number is {:,}".format(number))  # this will automatically add commas => The number is 1,000,000
print("The number is {:b}".format(number))  # displays number as binary
print("The number is {:o}".format(number))  # displays number as octal
print("The number is {:x}".format(number))  # displays number as hexadecimal
print("The number is {:e}".format(number))  # displays number as scientific notation

# random module
# import random
x = random.randint(1, 6)  # between 1 and 6
y = random.random()  # between 0 and 1.0

print()
print(x)  # 6
print(y)  # 0.9654803990742096

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)  # generates random choice from passed list
print(z)  # rock

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "j", "q", "k", "a"]
random.shuffle(cards)
print(cards)  # [4, 8, 7, 3, 9, 1, 'j', 5, 'q', 6, 'a', 2, 'k']

# Exception
try:
    value = 25
    value = value / 0
    print(value)
except ZeroDivisionError:
    print("You can't divide by 0!")
except ValueError:
    print("Enter only numbers please!")
except Exception as e:
    print(e)
    print("Something went wrong :c")
else:
    print(value)
finally:
    # This will always execute
    print("close the files")

# File Detection
# import os
path = "files/data.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")

# Reading File
print()
path = "files/data.txt"
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found.")

# Write a file
# "w" - writes text to a file and replaces already existing content of the file
# "a" - appends file with a new text
text = "Yooooooooooo\nSome Text\nHave a good one!\n"
with open(path, "a") as file:
    file.write(text)

# Copy a File
# import shutil
# copyfile() => copies contents of a file
# copy() => copyfile() + permission mode + destination can be a directory
# copy2() => copy() + copies metadata (file's creation and modification times)
shutil.copy2(path, "files/copy.txt")

# Move a file
source = "files/copy.txt"
destination = "files/copy/copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")


# Delete a File
path = "files/test.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("File was not found!")

# Delete Empty Directory
path = "files/test"
try:
    os.rmdir(path)
except FileNotFoundError:
    print("This directory was not found!")
except PermissionError:
    print("You do not have a permission to delete this.")
except OSError:
    print("You cannot delete that using that function!")
else:
    print(path + " was deleted!")

# Delete Directory containing files
path = "files/test"
try:
    shutil.rmtree(path)
except FileNotFoundError:
    print("This directory was not found!")
except PermissionError:
    print("You do not have a permission to delete this.")
except OSError:
    print("You cannot delete that using that function!")
else:
    print(path + " was deleted!")

# os.remove(path)  # delete a file
# os.rmdir(path)  # delete an empty directory
# shutil.rmtree(path)  # delete a directory containing files

# Modules
# import messages as msg
msg.hello()
msg.bye()

