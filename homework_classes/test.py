#!usr/bin/python

# 1. Գրե&#39;լ BigBell դասը, որը sound մեթոդի կանչի ժամանակ տպում է փոխ առ փոխ ding և dong բառերը,
# սկսելով ding-ից։

class BigBell:
  def __init__(self):
    self.__count = 0

  def sound(self):
    if (self.__count % 2 == 0):
      print("ding")
    else:
      print("dong")
    self.__count += 1
    return ""


# 2. Գրել MinMaxWordFinder դասը։ Այն պետք է կարողանա վերլուծել տեքստը և գտնել նրանում
# ամենամեծ և ամենափոքր երկարությամբ բառերը։ Տեքստը բաղկացած է նախադասություններից, որոնք
# ավելացվում են մշակման համար add_sentence մեթոդով։ shortest words մեթոդը վերադարձնում է
# տվյալ պահին ամենակարճ, longest_words մեթոդը՝ ամենաերկար, բառերի ցուցակը։ shortest_words-ի և
# longest_words-ի վերադարձրած բառերը պետք է տեսակավորված լինեն այբբենական կարգով։
# Եթե ամենակարճ բառերից մեկը հանդիպել է տրված նախադասություններում մի քանի անգամ, այն պետք է
# նույնքան անգամ կրկնվի ամենակարճ բառերի ցուցակում։ Ամենաերկար բառերն, ընդհակառակը, պետք է
# ցուցակի մեջ մտնեն առանց կրկնությունների։


class MinMaxWordFinder:
  def __init__(self):
    self.sentences = ""

  def add_sentence(self, sentence):
    self.sentences += sentence + " "
    return

  def shortest_words(self):
    return self.getWords("min")

  def longest_words(self):
    return self.getWords("max")

  def getWords(self, minMax):
    sList = self.sentences.split(" ")
    l = (len(word) for word in sList if word)
    f = filter(lambda x: len(x) == wL, sList)
    if (minMax == "min"):
      wL = min(l)
      words = list(f)
    elif (minMax == "max"):
      wL = max(l)
      words = set(f)

    return words

def main():
  bell = BigBell()
  bell.sound()
  bell.sound()
  bell.sound()

  finder = MinMaxWordFinder()
  finder.add_sentence("hello abc world qwert")
  finder.add_sentence("def asdf qwert")
  print(" ".join(finder.shortest_words()))
  print(" ".join(finder.longest_words()))

if __name__ == "__main__":
  main()
