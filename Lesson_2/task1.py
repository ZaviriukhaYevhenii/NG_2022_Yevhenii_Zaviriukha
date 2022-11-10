userInput = input("Enter string - ")
dictoonaryLetter = {}
existingLetters = set(userInput)

for element in existingLetters:
    dictoonaryLetter[element] = userInput.count(element)
print("Number of repetitions of each letter - ", dictoonaryLetter)

listKeys = list(dictoonaryLetter.keys())
listKeys.sort()
print("sorting quantity by letter - ", end="")

for values in listKeys:
    print(values, '-', dictoonaryLetter[values] , " ", end="")
    



