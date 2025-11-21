from stats import getNumWords, getCharDict, createDictList
import sys
def getBookText(bookPath):
    with open(bookPath) as f:
        fileContents = f.read()
    return fileContents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookPath = sys.argv[1]
    fileContents = getBookText(bookPath)
    numWords = getNumWords(fileContents)    
    charDict = getCharDict(fileContents)
    charList = createDictList(charDict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}")
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    for char in charList:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()
