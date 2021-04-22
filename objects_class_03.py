# Exercises
# Text Analysis

# You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can
# perform analysis on a given piece of text. Complete the class 'analysedText' with the following
# methods -

#     Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the
# following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?).
# Store the argument in "fmtText"
#     freqAll - returns a dictionary of all unique words in the text along with the number of their
# occurences.
#     freqOf - returns the frequency of the word passed in argument.

# The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise.
# Hint: Some useful functions are replace(), lower(), split(), count()

# class analysedText(object):

#     def __init__ (self, text):
#         pass

#     def freqAll(self):
#         pass

#     def freqOf(self,word):
#         pass


import sys


class analysedText(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


sampleMap = {'eirmod': 1, 'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1,
             'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}


def testMsg(passed):
    if passed:
        return 'Test Passed'
    else:
        return 'Test Failed'


print("Constructor: ")
try:
    samplePassage = analysedText(
        "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(
        testMsg(
            samplePassage.fmtText ==
            "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function ")
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap == sampleMap))
except:
    print("Error detected. Recheck your function ")
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))

except:
    print("Error detected. Recheck your function  ")
