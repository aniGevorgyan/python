#!/usr/bin/python

# Registration form
"""
  :input username, password, confirm password
  :output: success or error on registration process
"""
def registration():
  f = open("credentials.txt", "r")
  creds = f.read().splitlines()
  f.close()
  data = {}
  for i in creds:
    up = i.split(": ")
    data[up[0]] = up[1]
  myusername = input("Please enter an username: ")
  if myusername in data:
    mypassword = input("Please enter an password: ")
    if mypassword == data[myusername]:
      print("Hello", myusername)
    else:
      print("Invalid password")
  else:
    acc = input("Would you like to register(Y/N): ")
    if (acc == "N" or acc == "n"):
      print("Good luck to you!!!")
    if (acc == "Y" or acc == "y"):
      mypassword = input("Please enter an password: ")
      mypassword1 = input("Please re-enter an password: ")
      if (mypassword == mypassword1):
        data[myusername] = mypassword
        f = open("credentials.txt", "a")
        f.write(myusername + ": " + mypassword + "\n")
        f.close()
        print("You are registred.")
      else:
        print("The passwords are not equal. PLease try again.")
  return data


def main():
  registration()


if __name__ == "__main__":
  main()
