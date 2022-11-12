def userInput():
    string = input("Enter string - ")
    return string

def numbersLetters(string):
    from collections import Counter
    if(string == ""):
        return 0
    else:
        collection = Counter(string)
        print(collection)

numbersLetters(userInput())
