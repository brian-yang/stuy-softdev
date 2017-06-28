## Olivia Gallager and Brian Yang and Stiven Peter
## Softdev HW pd 6

import re

# read text
f = open("haha.txt", "r")
text = f.read()
f.close()

words = re.findall(r"[\w']+", text) # regex to get all the words

print "WORD FREQUENCIES"
print "============================"
# frequency of a specific word
# ============================
word = "chapter"

def checkWord(element):
        # count = result
        # return count + 1 if element == word else count
        return element.lower() == word

def wordCount():
        matching = filter(checkWord, words)
        return len(matching)

print "Frequency of word '" + word + "': " + str(wordCount())

print "Frequency of Groups of Words"

def checkWords(L):
        f = 0
        y = False
        for i in range(len(words)):
                if words[i] in L:
                        for x in range(len(L)):
                                if (L[x].lower() == words[i].lower()):
                                       y = True
                        if y == True:
                                f+=1
        return f
                                


def wordsCount(L):
        matching = filter(checkWords, L)
        return len(matching)


print " 'she loved': "
print wordsCount(["she","loved"]) 
print "\n"

# frequency of a list of words
# ============================
wordList = ["she", "he", "her", "him", "they", "them"]

def checkWordList(element):
        if element.lower() in wordList:
                return element.lower()
        else:
                return ''

def wordCountList():
        freqStr = ""
        frequencies = map(checkWordList, words)
        for i in range(len(wordList)):
                freqStr += wordList[i] + ": " + str(frequencies.count(wordList[i])) + "\n"
        return freqStr

print "Wordlist: " + str(wordList)
print wordCountList()

# most frequent word
# ==================
def getFrequencies(result, element):
        if element.lower() not in result:
                result[element.lower()] = 1
        else:
                result[element.lower()] += 1

        return result

def mostFrequent():
        frequencyDict = reduce(getFrequencies, words, {}) # function, iterable list, initializer (initial value of result in checkWord)
        maxFrequency = 0
        keys = frequencyDict.keys()
        for i in range(len(keys)):
                if frequencyDict[keys[i]] > maxFrequency:
                        maxWord = keys[i]
                        maxFrequency = frequencyDict[keys[i]]
        return (maxWord, maxFrequency)

mostFrequentData = mostFrequent()
print "Most frequent word: '" + mostFrequentData[0] + "' (appears " + str(mostFrequentData[1]) + " times)"
