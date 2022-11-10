userInput = input("Enter string - ")
dictoonaryLetter = {}
existingLetters = set(userInput)

for element in existingLetters:
    dictoonaryLetter[element] = userInput.count(element)
print("Number of repetitions of each letter: ", dictoonaryLetter)

listKeys = list(dictoonaryLetter.keys())
listKeys.sort()
print("Sorting quantity by letter: ", end="")

for values in listKeys:
    print(values, '-', dictoonaryLetter[values] , " ", end="")

print("\nLetters were sorted by number: ", dict(sorted(dictoonaryLetter.items(), key=lambda item:item[1], reverse=True)))
    



