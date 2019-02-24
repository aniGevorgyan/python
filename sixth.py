#! usr/bin/python3.6

# 1.

number = int(input("Type number: "))
word = input("Type word: ")
list = []

for i in range(number):
    s = input("Sentence here: ")
    list.append("%d : %d" %(i, s.count(word)))
print("\n".join(list))

# 2.

number2 = int(input("Type number: "))
list2 = []

for i in range(number2):
    s = input("Sentence here: ")
    list2.append(s)
list2 = list2[::-1]
print("\n".join(list2))

#3.

sentence = "Mary and Samantha arrived at the bus station early but waited until noon for the bus."
list = sentence.split()

w = input("Word here: ")
while(w != 'End'):
    if(w.isdigit()):
        print(list[int(w)])
        w = input("Word here: ")
    else: break
print("Finish")

#4.

sentence = "Mary and Samantha arrived at the bus station early but waited until noon for the bus."
list = sentence.split()

w = input("Word here: ")
while(w != 'End'):
    if(w.isdigit()):
        if('a' in list[int(w)]):
            print("Yes")
        else:
            print("No")
        w = input("Word here: ")
    else: break
print("Finish")