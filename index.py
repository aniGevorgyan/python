#!/usr/bin/python 3.7.2
"""
  :input name, surname, date of birth:
  :output: age
"""
import datetime


def getAge():
  now = datetime.datetime.now()
  name = input("Please enter your name\n")
  surname = input("Please enter your surname\n")
  dob = input("Please enter your birth of date\n")
  age = now.year - int(dob)
  print(name + ' ' + surname + ' ' + 'You are ' + str(age) + ' years old')


# Program enter point
def main():
  getAge()

if __name__ == "__main__":
  main()
