def countWordsFromFile():
    fileName = input("Please enter the file name: ")
    file = open(fileName, "r+")

    wordCount = 0
    for line in file:
        words = line.split()
        wordCount = wordCount + len(words)
        
    print("The number of words in the file - " + fileName + ", is: ")
    print(wordCount)

countWordsFromFile()