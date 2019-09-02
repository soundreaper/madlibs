import sys
from termcolor import colored, cprint

'''
Pizza:

Pizza was invented by a [adjective] [nationality] chef named [person]. To make pizza, you need to take a lump
of [noun], and make a thin, round [adjective] [noun]. Then you [adverb] [verb] it with [adjective] sauce, [adjective] cheese,
and fresh chopped [plural noun]. Next you have to bake it in a very hot [noun]. When it is done, cut it
into [number] [shapes]. Some kids like [food] pizza the best, but my favorite is the [food] pizza. If I could, I would
eat pizza [number] times a day!
'''

partOfSpeechArray = ['adjective', 'nationality', 'person', 'noun', 'adjective', 'noun', 'adverb', 'verb', 'adjective', 'adjective', 'plural noun',
'noun', 'number', 'shape', 'food', 'food', 'number']

inputArray = []

# DIFFERENT PARTS OF SPEECH + COLOR ASSIGN
def partsOfSpeech(input, counter):
    for items in partOfSpeechArray:
        if partOfSpeechArray[counter] == "adjective":
            colorText = colored(input, 'red')
            return colorText
        elif partOfSpeechArray[counter] == "nationality" and "adverb":
            colorText = colored(input, 'green')
            return colorText
        elif partOfSpeechArray[counter] == "person":
            colorText = colored(input, 'yellow')
            return colorText
        elif partOfSpeechArray[counter] == "noun" and "plural noun":
            colorText = colored(input, 'blue')
            return colorText
        elif partOfSpeechArray[counter] == "verb":
            colorText = colored(input, 'grey')
            return colorText
        elif partOfSpeechArray[counter] == "number":
            colorText = colored(input, 'magenta')
            return colorText
        elif partOfSpeechArray[counter] == "shape":
            colorText = colored(input, 'cyan')
            return colorText
        elif partOfSpeechArray[counter] == "food":
            colorText = colored(input, 'white')
            return colorText

    
# VALID TEXT CHECK
# add for whitespace
def textVerification(input):
    if input.isalpha():
        return True
    else:
        return False

# TEST
def test():
    running = 0
    while running < 17:
        textInput = input("Enter a " + partOfSpeechArray[running] + ": ")
        check = textVerification(textInput)
        if check == True:
            inputArray.append(partsOfSpeech(textInput, running))
            running += 1
        else:
            print("That input was invalid.\n")
    
    madLib = f"""\nPizza was invented by a {inputArray[0]} {inputArray[1]} chef named {inputArray[2]}. To make pizza, you need to take a lump
of {inputArray[3]}, and make a thin, round {inputArray[4]} {inputArray[5]}. Then you {inputArray[6]} {inputArray[7]} it with {inputArray[8]} sauce, {inputArray[9]} cheese,
and fresh chopped {inputArray[10]}. Next you have to bake it in a very hot {inputArray[11]}. When it is done, cut it
into {inputArray[12]} {inputArray[13]}. Some kids like {inputArray[14]} pizza the best, but my favorite is the {inputArray[15]} pizza. If I could, I would
eat pizza {inputArray[16]} times a day!"""

    print(madLib)

test()


