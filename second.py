#!/usr/bin/python 3.7.2

# Homework 1: Reverse 2 numbers
"""
  :input number_1, number_2
  :output: number_2, number_1
"""

print("Homework 1: Reverse 2 numbers")

number_1 = 77
number_2 = 66
print(number_1, number_2)
number_1 = number_1 + number_2
number_2 = number_1 - number_2
number_1 = number_1 - number_2
print(number_1, number_2)

# Homework 2: Check if the word ends with 'ard'

print("-------------------------------")
print("Homework 2: Check if the word ends with 'ard'")

word = input("Please enter some word: ")
end = "ard"
if (word[-3:] == end):
  print("Word ends with %s" % (end))
else:
  print("Word doesn\'t ends with %s" % (end))

# Homework 3: Check if user is adult

print("-------------------------------")
print("Homework 3: Check if user is adult")

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
dob = input("Please enter your date of birth:")
age = 2019 - int(dob)
print("%s %s Your age is %d, less than 18" % (name, surname, age)) if (age < 18) else print(
  "%s %s Your age is %d, more then 18" % (name, surname, age))

# Homework 4: Return position on first letter of name and surname

print("-------------------------------")
print("Homework 4: Return position on first letter of name and surname")

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
str = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]


def checkLetter(letter, type):
  if (letter.lower() in str):
    print('Your %s first letter position is %s' % (type, str.index(letter.lower())))
  else:
    print("Error: You can type only English letters!")


checkLetter(name[0], 'name')
checkLetter(surname[0], 'surname')

# Homework 5: Print the difference of the max_var and min_var variables

print("-------------------------------")
print("Homework 5: Print the difference of the max_var and min_var variables")

a = int(input("Type some number: "))
b = int(input("Type some number: "))
c = int(input("Type some number: "))

max_var = a
min_var = a

if (b < min_var):
  min_var = b
if (c < min_var):
  min_var = c
if (b > max_var):
  max_var = b
if (c > max_var):
  max_var = c
print(max_var - min_var)

# Homework 6: Print the variables in sorted way

print("-------------------------------")
print("Homework 6: Print the variables in sorted way")

a = int(input("Type some number: "))
b = int(input("Type some number: "))
c = int(input("Type some number: "))

print(a, b, c)

# sort numbers
if (a > b):
  a, b = b, a
if (a > c):
  a, c = c, a
if (b > c):
  b, c = c, b

print(a, b, c)
