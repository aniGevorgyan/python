#!/usr/bin/python 3.7.2

# 1.
print("-------------- Task 1 -----------------")
a = input("Check temperature: ")
a = float(a)
if (a < 15.5):
  print("It's cold")
elif (a >= 33):
  print("It's hot")
else:
  print("It's fine")

# 2.
print("-------------- Task 2 -----------------")
a = input('Password here: ')
b = input('Confirm password: ')
if (len(a) < 8):
  print("Password is too short, it should contains min 8 symbols!")
elif (a != b):
  print("Password and confirm password do not match!")
else:
  print("Password is normal")

# 3.
print("-------------- Task 3 -----------------")
a = "Some text"
while (a != ""):
  a = input("Your text here: ")
print("Program was finished, cause you entered empty line")

# 4.
print("-------------- Task 4 -----------------")
a = input("Enter number: ")
b = abs(int(float(a)))
i = c = 1
while (i <= b):
  c *= i
  i += 1
print(c)

# 5.
print("-------------- Task 5 -----------------")
a = input("Enter number: ")
b = abs(int(float(a)))
i = 1
while (i <= b):
  print("%d - %d" % (i, pow(i, 3)))
  i += 1

# Extra HomeWorks

# 1. Գրեք ծրագիր, որը յուրաքանչյուր ներածված տողից արտածում է տրված համարով տառը։ Դա կարող է
# օգտագործվել, օրինակ, հապավումների կառուցման կամ ակրոստիքոսներ կարդալու համար։ Եթե ինչ-որ տողեր
# շատ կարճ են, և նրանցում տվյալ համարով սիմվոլ չկա, ապա այդպիսի տողերը արտածման ժամանակ
# պարզապես պետք է բաց թողնել։

print("-------------- Task 1 -----------------")

word = string = ''
words = []
rowsCount = int(input("Enter rows count: "))
for i in range(rowsCount):
  word = input("Your word here: ")
  words.append(word)
index = int(input("Enter letter index: ")) - 1
for i in words:
  string += i[index]
print(string)

# 2. Դուք պատրաստվում եք գնալ խանութ և գրի եք առնում, թե ինչ և որքան պետք է գնել։ Գրեք ծրագիր, որը
# նախ կարդում է գնումների քանակը, ապա հերթով յուրքանաչյուր գնվող ապրանքի անվանում և քանակը
# (ամբողջ թիվ) առանձին տողերում, ապա արտածում է դրանք հակառակ կարգով, արտածելով յուրաքանչյուր
# ապրանքի անունը և քանակը մեկ տողում իրարից անջատելով մեկ բացատով։

print("-------------- Task 2 -----------------")

product = count = row = ''
products = reversedList = []
productCount = int(input("Enter rows count: "))
for i in range(productCount):
  product = input("Product name: ")
  count = input("Product count: ")
  row = product + " " + count
  products.append(row)
reversedList = products[::-1]
for i in reversedList:
  print(i)

# 3. Կադրերի բաժնի պետը ուզում է իմանալ, թե նույն ազգանունն ունեցող քանի տղամարդ է աշխատում
# կազմակերպությունում։ Նա ունի ազգանունների ցուցակ, և այդ ցուցակի հիման վրա պետք է հաշվել այլ
# ազգանունների հետ համընկնող ազգանունների քանակը։

print("-------------- Task 3 -----------------")

set = set()
count = 0

list = ["Ivanov", "Sidorov", "Petrov", "Ivanov", "Petrov", "Petrov"]
for x in list:
  set.add("%s : %d" % (x, list.count(x)))
for x in set:
  if (int(x[-1]) > 1):
    count += int(x[-1])
print(count)

# 4. Գրեք «Ցուլեր և կովեր» խաղի մեկ փուլը մշակող ծրագիր: Օգտատերը մուտքագրում է երկու տող: Պետք է
# երաշխավորվի, որ այդ տողերը նույն երկարության են և որ տողերից յուրաքանչյուրի բոլոր նիշերը տարբեր
# են: Անհրաժեշտ է առանձին արտածել ցուլերի քանակը, այն է` երկու տողերում առկա և նույն դիրքը
# զբաղեցնող սիմվոլների քանակը, և կովերի քանակը, այն է` երկու տողերում առկա, սակայն տարբեր դիրք
# զբաղեցնող սիմվոլների քանակը:

print("-------------- Task 4 -----------------")

bull = cow = 0
duplicatedLetter = 0

word1 = input("Enter first word: ")
word2 = input("Enter first word: ")

for i in word1:
  if (word1.count(i) > 1):
    duplicatedLetter = 1

for i in word2:
  if (word2.count(i) > 1):
    duplicatedLetter = 1

if (len(word1) != len(word2)):
  print("Please type words with same length!")
elif (duplicatedLetter):
  print("All letters should be unique!")
else:
  for i in range(len(word1)):
    for j in range(len(word2)):
      if (word1[i] == word2[j] and i == j):
        bull += 1
      elif (word1[i] == word2[j]):
        cow += 1
  print("Bulls count are: %d" % (bull))
  print("Cows count are: %d" % (cow))

# 5. Շատ ինտերնետային սերվիսներում գրանցման ժամանակ պետք է նշել օգտատիրոջ ցանակլի անունը, ընդ
# որում անվան մեջ թույլատրվում է օգտագործել միայն լատինական տառեր, թվեր և «_» նշանը։
# Գրեք ծրագիր, որը կստուգի համապատասխանում է, արդյո՞ք, տողը այդպիսի սերվիսում որպես օգտատիրոջ
# անուն ծառայելու պահանջներին։

print("-------------- Task 5 -----------------")

username = input("Enter your username: ")
message = ''
for i in username:
  if (i.isdigit() or i.isalpha() or i == '_'):
    message = "Correct Username"
  else:
    message = "Invalid character " + i
    break
print(message)
