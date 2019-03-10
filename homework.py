#!/usr/bin/python 3.7.2
from math_util import myFactorial

# 1. Գրել ֆունկցիա, որը կընդունի 1 պարամետր՝ n, և կվերադարձնի բառարան, որի key-երն են 1-ից մինչև n֊ը, իսկ value֊ները
# դրանց համապատասխան ֆակտորիալները։

def getFactorial(n):
  md = {}
  for i in range(1, n + 1):
    md[i] = myFactorial(i)
  return md


# 2. Կատարել հետևյալ քայլերը․
# 	- Մուտքագրել նախադասություն
# 	- Հաշվել դրա տառերի քանակը /առանց օգտվելու տողի որևիցե ֆունկցիայից/
# 	- Տպել նախադսությունը, ամբողջությամբ մեծատառերով։
# 	- Տպել նախադասությունը, որի յուրաքանչյուր բառի վերջին տառը մեծատառ է
# 	- Ստանալ լիստ, որի էլեմենտները տվյալ նախադասության կենտ երկարություն ունեցող բառերն են
# 	- Վերադարձնել նախադասությունում ամենաշատ և ամենաքիչ հանդիպող տառերը/1ական/
# 	- Դասավորել բառերը ֆայլի մեջ այբբենական կարգով, որոնց դիմաց գրել համապատասխան հակադարձ բառերը /օր․ այո - ոյա/

def getLettersLenth(ms):
  sLenth = 0
  for i in ms:
    if i in ('abcdefghijklmnopqrstuvwxyzABSDEFGHIJKLMNOPQRSTUVWXYZ'):
      sLenth += 1
  return sLenth

def getUpperSentence(ms):
  sUpper = ''
  for i in ms:
    sUpper += i.upper()
  return sUpper

def capitalizeLastLetter(ms):
  result = ""
  for word in ms.split():
    result += word[:-1] + word[-1].upper() + " "
  return result

def getOdds(ms):
  listOdd = []
  for i in ms.split():
    if(len(i)%2 == 1):
      listOdd.append(i)
  return listOdd

def getMaxAndMinCounts(ms):
  md = {}
  for i in ms:
    if (i.isalpha()):
      md[i] = ms.count(i)
  max = 0
  min = len(ms)
  max_key = min_key = ""
  for k, v in md.items():
    if (max < v):
      max = v
      max_key = k
    if (min > v):
      min = v
      min_key = k
  return "Max - " + max_key +":" + str(max), "Min - " + min_key +":" + str(min)

def writeInFile(ms):
  sSorted = sorted(ms.split())
  f = open("test.txt", "w")
  for i in sSorted:
    f.write(i + " - " + i[::-1] + "\n")
  return sSorted

def main():
  ms = input("Your sentence here: ")
  print(getFactorial(14))
  print(getLettersLenth(ms))
  print(getUpperSentence(ms))
  print(capitalizeLastLetter(ms))
  print(getOdds(ms))
  print(getMaxAndMinCounts(ms))
  writeInFile(ms)

if __name__ == "__main__":
  main()
