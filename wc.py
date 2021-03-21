import sys


def main(argv):
    file = argv[1]
    textString = "\n".join(open(file).readlines())
    print(textString)
    print(type(textString))
    wordlist = textString.split()

    wordset = set()
    for word in wordlist:
        wordset.add(word)

    wordFreq = []
    for w in wordset:
        wordFreq.append(wordlist.count(w))

    print("String\n" + textString + "\n")
    print("Uniq words\n" + str(wordset) + "\n")
    print("Frequencies\n" + str(wordFreq) + "\n")
    print("Pairs\n" + str(list(zip(wordlist, wordFreq))))

if __name__ == "__main__":
    main(sys.argv)
