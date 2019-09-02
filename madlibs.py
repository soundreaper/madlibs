import sys
from termcolor import colored, cprint

'''
Pizza:

Pizza was inveted by a [adjective] [nationality] chef named [person]. To make pizza, you need to take a lump
of [noun], and make a thin, round [adjective] [noun]. Then you cover it with [adjective] sauce, [adjective] cheese,
and fresh chopped [plural noun]. Next you have to bake it in a very hot [noun]. When it is done, cut it
into [number] [shapes]. Some kids like [food] pizza the best, but my favorite is the [food] pizza. If I could, I would
eat pizza [number] times a day!
'''

inputArray = ['adjective', 'nationality', 'person', 'noun', 'adjective', 'noun', 'adjective', 'adjective', 'plural noun'
'noun', 'number', 'shape', 'food', 'food', 'number']

# DIFFERENT PARTS OF SPEECH + COLOR ASSIGN
def partsOfSpeech(input):
    for items in inputArray:
        if items == "adjective":
            colorText = colored(input, 'red')
            return colorText
        elif items == "nationality":
            colorText = colored(input, 'green')
            return colorText
        elif items == "person":
            colorText = colored(input, 'yellow')
            return colorText
        elif items == "noun" | "plural noun":
            colorText = colored(input, 'blue')
            return colorText
        elif items == "number":
            colorText = colored(input, 'magenta')
            return colorText
        elif items == "shape":
            colorText = colored(input, 'cyan')
            return colorText
        elif items == "food":
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
    running = 1
    while running < 16:
        textInput = input("Enter a word: ")
        check = textVerification(textInput)
        if check == True:
            print(partsOfSpeech(textInput))
            running += 1
        else:
            print("That input was invalid.")

test()


