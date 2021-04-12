# Task 1 - Write a python script to print your name and age

name = input("Enter your name")
age = int(input("Enter your age"))

print("Your name is : ", name, " Your age is : ", age)

# Task 2 - Create a list of your 5 favorite movies and store it in the variable

movies = []
for i in range(5):
    movie = input(" Enter your favorite movies")
    movies.append(movie)

print("Your 5 Fav movies are : ", movies)

# Task 3 - Write a Python program to display the first and last colors from the following list.

color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[-1])

# Task 4 - Write a Python script to add a key to a dictionary
numbers = {0: 10, 1: 20}
numbers[2] = 30
print(numbers)

# Task 5 - Write a Python program to calculate body mass index.
name = input("enter your name")
weight = float(input("enter your weight in kg"))
height = float(input("enter your height in meter"))

bmi = weight/height*height
print(name, "'s BMI is ", bmi)

# Task 6 - Guess a number game - between 1 to 9.

guessnumber = 7
while True:
    userguess = int(input("Enter your guess number"))
    if userguess == guessnumber:
        print("Well guessed!")
        break

# Task 7 - Create a tuple with different data types

tuple1 = ("hello world", 134, True, 40.4)

print(tuple1)

# Task 8 - Create a list of 5 city names and convert it into tuples.

city = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Copenhagen"]
print("Type of city variable : ", type(city))
citytuple = tuple(city)
print("Type of citytuple variable : ", type(citytuple))
print("City Tuple : ", citytuple)

# Task 9 - Remove duplicated from the list
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a = list(dict.fromkeys(a))
print(a)

# Task 10 - Accept a string from user and remove the characters which have odd index values of a given string and print them.

str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(len(str1)):
    if (i % 2 == 0):
        str2 = str2 + str1[i]

print("Original String :  ", str1)
print("Final String :     ", str2)



