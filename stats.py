def getNumWords(fileContents):
    wordList = fileContents.split()
    return len(wordList)

def getCharDict(fileContents):
    charDict = {}
    for char in fileContents.lower():
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    return charDict

def getNum(num):
  return num['num']

def createDictList(charDict):
    dictList = []
    for char in charDict:
        dictList.append({ "char": char, "num": charDict[char]})
    dictList.sort(key=getNum, reverse=True)
    return dictList
