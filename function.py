def countWordsFromFile():
    fname = input("enter the file name: ")
    noOfWords = 0
    file = open(fname,"r")
    for line in file:
        words = line.split()
        noOfWords = noOfWords+len(words)
    print("number of words: ")
    print(noOfWords)

countWordsFromFile()