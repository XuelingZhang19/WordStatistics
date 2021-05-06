import sys
import re


def main(argv):
    file = argv[1]
    textString = open(file).read()
    wc(textString)
    lc(textString)
    cc(textString)
    rl(textString)



#===========feature 1: Frequency of each unique word========
def wc(textString):
    wordlist = textString.split()
    wordset = set()
    for word in wordlist:
        wordset.add(word)
    wordFreq = []
    for w in wordset:
        wordFreq.append(wordlist.count(w))

    print("===========String================\n" + textString + "\n")
    # print("Uniq words\n" + str(wordset) + "\n")
    print("==========feature 1: Uniqi word and frequency==========")
    # print("Frequencies\n" + str(wordFreq) + "\n")
    print(str(list(zip(wordset, wordFreq))) + "\n")

# ===============featrure 2: LineCount =================
def lc(textString):
    lineCount = textString.split("\n")
    print("==========feature 2: Number of lines==========\n" + "Number of lines: " + str(len(lineCount)) + "\n")

#===============featrure 3: CharCount =================
def cc(textString):
    print("==========feature 3: Number of Characters==========\n" + "Number of Characters: " + str(len(textString)) + "\n")


#===============featrure 4: replace =================
def rl(textString):
    print("==========feature 4: Replacement==========\n")

    org = input("Enter the word needs to be replaced: ")
    target = input("Enter the word you want to replace with: ")
    print("The program will replace \"" + org + "\" with \"" + target + "\"" + '\n')

    wordlist = textString.split(" ")
    newWorlList = []
    print("=====Original text:" + '\n')
    print(textString)
    for item in wordlist:
        word = re.search(r'[a-z]+', item).group(0)
        if word == org:
            newWorlList.append(item.replace(org, target))
        else:
            newWorlList.append(item)

    print("\n" + "=====After replacement:" + "\n")
    print(" ". join(newWorlList))


if __name__ == "__main__":
    main(sys.argv)
