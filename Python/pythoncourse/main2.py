# ------------------------------- walrus operator :=

# happy = True
# print(happy)

print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?:")
#     if food == "quit":
#         break
#     foods.append(food)

# foods = list()
# while (food := input("What food do you like?")) != "quit":
#     foods.append(food)

# print()
# print(foods)

# assigning function to a variable


def hello():
    print("Hello")


hi = hello
print(hi)
print(hello)
print(hi())

pizda = print
pizda("JD")

# ---------------------------------------- High Order Functions
# 1. accepts a function as an argument
# OR
# 2. returns a function

# 1


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello2(func):
    text = func("Hello")
    print(text)


hello2(loud)  # HELLO
hello2(quiet)  # hello
print()

# 2


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))  # 5.0


# ------------------------------------ lambda
# lambda parameters:expression

# def double(x):
#    return x * 2

def double(x): return x*2
def multiply(x, y): return x * y
def full_name(first_name, last_name): return first_name + " " + last_name


print(double(5))
print(multiply(5, 5))
print(full_name("John", "Fuck"))


def age_check(age): return True if age >= 18 else False


print(age_check(15))  # False
print(age_check(18))  # True


#--------------------------------- Sort
# a list
studentsList = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krab"]

print()
studentsList.sort()  # sorts the list
for i in studentsList:
    print(i)

studentsList.sort(reverse=True)  # sorts the list in reverse order

# in tuple
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

sorted_students = sorted(students)

for i in sorted_students:
    print(i)

# List of tuples
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]


def grade(grades): return grades[1]


students.sort(key=grade)

print(grade(("JD", "James", 33)))
print()
for i in students:
    print(i)


def age(ages): return ages[2]


students.sort(key=age)

print()
for i in students:
    print(i)


# ---------------------------------- map()
# applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# 1 USD = 4.04 PLN
USD_TO_PLN = 4.04


def to_pln(items): return (items[0], items[1] * USD_TO_PLN)
def to_usd(items): return (items[0], items[1] / USD_TO_PLN)


store_pln = list(map(to_pln, store))
store_usd = list(map(to_usd, store_pln))

print("\n In PLN: ")
for i in store_pln:
    print(i)

print("\n In USD: ")
for i in store_usd:
    print(i)

# -------------------------------- filter()
# creates a collection of elements from an iterable,
# for which a function returns true
#
# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Katarina", 16),
           ("Ross", 20),
           ("Joey", 15),
           ("Hugo", 57),
           ]


def age(person): return person[1] >= 18


drinking_buddies = list(filter(age, friends))

print()
for i in drinking_buddies:
    print(i)
