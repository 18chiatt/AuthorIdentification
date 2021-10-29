import os
from pathlib import Path
import string

words = list( map(lambda x: x.strip(), open('./wordlist.txt', 'r').readlines() ) )
wordMap = {word: i for i,word in enumerate(words)}

WORD_COUNT_PER_SECTION = 1000
translation = str.maketrans('', '', string.digits + string.whitespace + string.punctuation + '—-,"”“’' + "'")

def getFrequency(section):
    frequency = [ 0 for _ in range(len(words))]
    for word in section:
        if word in wordMap:
            frequency[wordMap[word]] += 1
    return [frequency[i]/WORD_COUNT_PER_SECTION for i in range(len(frequency))]

def getWordSections(bookPath):
    sections = []
    file = open(bookPath, 'r', encoding='utf-8')
    currSection = []
    currLength = 0
    for line in file.readlines():
        for word in line.split():
            word = word.translate(translation).lower()
            if not word:
                continue
            if currLength == WORD_COUNT_PER_SECTION:
                sections.append(currSection)
                currSection = []
                currLength = 0
            currSection.append(word)
            currLength+=1
    return sections[1:-1] #Ignore first 1,000 words and last 1,000 words

def writeFileStats(bookPath, outputFile):
    wordSections = getWordSections(bookPath)
    print("    Writing book from path:", str(bookPath))
    for section in wordSections:
        frequency = getFrequency(section)
        print(frequency, file=outputFile)
    

def fromAuthorDirectory(path):
    authorName = str(path).split('\\')[1]
    print("Working on", authorName)
    if not Path('./formatted/' + authorName):
        os.makedirs("./formatted/" + authorName)
    outputFile = open('./formatted/' + authorName, 'w')
    for book in path.iterdir():
        writeFileStats(book,outputFile)



if __name__ == '__main__':
    p = Path('./data')
    if not Path('./formatted').exists():
        os.makedirs('./formatted')
    for x in p.iterdir():
        fromAuthorDirectory(x)

    