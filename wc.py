import sys


def main(argv):
    file = argv[1]
    textString = open(file).read()


    #===========feature 1: frequency of each unique word========
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


    #===============featrure 2: LineCount =================
    lineCount = textString.split("\n")
    print("==========feature 2: Number of lines==========\n" + "Number of lines: " + str(len(lineCount)))




if __name__ == "__main__":
    main(sys.argv)
