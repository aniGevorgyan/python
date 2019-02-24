#!/usr/bin/python 3.7.2

countOfNumbers = 0
countOfLetters = 0
countOfSpecialChars = 0
countOfVowels = 0
matchCount = 0

vowels = 'aeiou'
sentence = "For instance, if a bank receives $500 as demand deposits and $200 as time deposits during the given period" \
           " and the reserve requirement ratio is 10%. The reserve computation will be as follows:"
for k in sentence:
  if (k.isdigit()):
    countOfNumbers += 1
  if (k.isalpha()):
    countOfLetters += 1
  if (not k.isdigit() and not k.isalpha()):
    countOfSpecialChars += 1
  if (k in vowels):
    countOfVowels += 1

# task 1 Count of numbers
print("--------------1----------------")
print(countOfNumbers)
# task 2 Count of letters
print("--------------2----------------")
print(countOfLetters)
# task 3 Count of symbols
print("--------------3----------------")
print(countOfSpecialChars)
# task 4 Count of vowels
print("--------------4----------------")
print(countOfVowels)

letter = input("Type some letter: ")
for k in sentence:
  if (k.lower() == letter.lower()):
    matchCount += 1

# task Count of entered word in sentence
print("--------------5----------------")
print(matchCount)

# task 6 Encode entered word in sentence

words = input("Type word which you want to encode: ")
splitedWords = words.split()
for i in splitedWords:
  if (i in sentence):
    sentence = sentence.replace(i, "*" * len(i))

print("--------------6----------------")
print(sentence)
