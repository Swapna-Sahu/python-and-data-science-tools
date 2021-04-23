# Task 1 : Checking type of number

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "-", "Fizz Buzz")
    elif num % 5 == 0:
        print(num, "-", "Buzz")
    elif num % 3 == 0 and num != 3:
        print(num, "-", "Fizz")
    else:
        print(num)


fizz_buzz(5)

# Task 2 : try and except error for index


try:
    random = [5, 10, 20]
    print(random[2])
    print(random[3])
except IndexError as e:
    print(e)


# Task 3 : Create a class of Jet inventory with two arguments i.e name and country. Also add the minimum 2 items in
# the class and print them.

class Jet:
    def __init__(self, name, country):
        self.jet_name = name
        self.country = country

    def details(self):
        print(self.jet_name, self.country)


new_jet = Jet("Jet Airways", "India")
new_jet.details()

# Task 5 - Write a Python script to check whether a given key already exists in a dictionary.

song_info = {"1": "album", "2": "rating", "3": "singer", "4": "writer", "5": "musician",
             "6": "released", "7": "genre", "8": "duration", "9": "recorded", "10": "producer"}

for key, value in song_info.items():
    print(key, value)


def guess_key(input_key):
    if input_key in song_info:
        print(f'user input key -  {input_key}  is present')
    else:
        print("False, No such key found!")


user_key = input("which key do you want to guess?\n")
print('user_key ', user_key)
guess_key(user_key)


# Task 6 - Write a function called showNumbers that takes a parameter called limit. It should print all the numbers
# between 0 and limit with a label to identify the even and odd numbers.

def show_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(i, "-", "Even")
        else:
            print(i, "-", "Odd")


show_numbers(9)


# Task 8 - Create a class named Person, with firstname and lastname properties, and a print name method.

class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def full_name(self):
        print(f'Fullname is : {self.first_name}  {self.last_name}')


my_name = Person("Swapna", "Sahu")
my_name.full_name()

# Task 9 - Write a program asks for numeric user input. Instead the user types characters in the input box. The
# program normally would crash. But write try-except block so it can be handled properly.


try:
    user_input = int(input("Enter any number"))
    print(user_input)
except ValueError:
    print("Invalid input. Enter only number ")


# Task 10 - Write a Python program to create two empty classes, Student and Marks. Now create some instances and
# check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of
# the built-in object class or not.

class Student:
    pass


class Marks:
    pass


student1 = Student()
mark1 = Marks()

print(type(student1))
print(type(mark1))
print(isinstance(student1, Student))
print(isinstance(mark1, Marks))
