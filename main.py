import string
import re

# Returns the content of a text file as a string


def readFromFile(file):
    f = open(file, 'r')
    return f.read()

# Returns whether the given word is a stopword


def stopWord(word):
    f = open('common-english-words.txt', 'r')
    stopwords = f.read().split(',')
    return word in stopwords

# Returns the list of unique words in a string, ignoring punctuation and stopwords


def getWordList(text):
    unprocessedWords = text.split()
    processedWords = {}
    for word in unprocessedWords:
        word = word.strip(string.punctuation + "\n\r\t")
        word = word.lower()
        if not stopWord(word):
            if word in processedWords:
                processedWords[word] += 1
            else:
                processedWords[word] = 1
    return processedWords

# Returns a dictionary that maps words to a list of tupples of the form (filename, count)


def indexFiles(files):
    indexer = {}
    for file in files:
        text = readFromFile(file)
        wordList = getWordList(text)
        for word in wordList:
            if word in indexer:
                indexer[word].append((file, wordList[word]))
            else:
                indexer[word] = [(file, wordList[word])]
    return indexer


fileList = ["DataAssignment4/Text1.txt", "DataAssignment4/Text2.txt", "DataAssignment4/Text3.txt",
            "DataAssignment4/Text4.txt", "DataAssignment4/Text5.txt", "DataAssignment4/Text6.txt"]

## Task C part 1
index = indexFiles(fileList)
#print(index)


## Query Claim
def queryClaim():
    result = []
    for word in index:
        if word == "claim":
            result.append((word, index[word]))
    return result
#print(queryClaim())


## Query claim*
def queryClaimStar():
    result = []
    for word in index:
        if re.search("claim*", word):
            result.append((word, index[word]))
    return result
print(queryClaimStar())

## Query claims of duty
def queryClaimsOfDuty():
    claims = []
    duty = []
    for tupple in index["claims"]:
        claims.append(tupple[0])
    for tupple in index["duty"]:
        duty.append(tupple[0])
    return list(set(claims) & set(duty))
#print(queryClaimsOfDuty())

