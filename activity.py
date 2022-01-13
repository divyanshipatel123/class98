
def countWords():
    fileN = input('Enter file name: ')
    file = open(fileN,'r')
    numWords = 0
    for line in file:
        words = line.split()
        numWords += len(words)
    print('Number of words are : ',numWords)

countWords()
        