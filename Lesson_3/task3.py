def userInput():
    userEnterString = input("Enter string - ")
    return userEnterString

def valueLetters(element, string):
    dictoonaryLetters = {}
    dictoonaryLetters[element] = string.count(element)
    return str(dictoonaryLetters[element])


def definitionLetters(stringExample):

    uniqueLetters = set(stringExample)
    listLetters = uniqueLetters

    uniqueLetters = (list(map(lambda element: valueLetters(element, stringExample), uniqueLetters)))

    numbersLetters = dict(zip(listLetters, uniqueLetters))
    print("The number of each letter in the line - " + str(numbersLetters))
    

definitionLetters(userInput())
