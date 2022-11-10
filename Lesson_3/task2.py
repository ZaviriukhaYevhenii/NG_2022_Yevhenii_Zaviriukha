def inputUserString():
    userString = input("Enter string - ")
    return userString

def sortUserString(string):
    res = ' '.join(sorted(string))
    print("sort string - ", res)

def lengthUserString(string):
    print("Length user string - " + str(len(string)))
    
def vowelsConsonantsLetters(string):
    vowelsLetters = ['a','e','i','o','u','y']
    ConsonantsLetters = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    numbers = int(input("Enter function: 1 - Vowels| 2- Consonants - "))
    string12 = ""
    if(numbers == 1):
        for index in range(len(vowelsLetters)):
            for element in range(len(string)):
                if(string[element] == vowelsLetters[index]):
                    string12 += string[element] + " "
            index += 1
        print(str(string12)) 
    if(numbers == 2):
        for index in range(len(ConsonantsLetters)):
            for element in range(len(string)):
                if(string[element] == ConsonantsLetters[index]):
                    string12 += string[element] + " "
            index += 1
        print(str(string12)) 

def separationWords(string):
    userList = string.split(' ')
    userList.reverse()
    print("Separation of words is the opposite conclusion: ", userList)

def inputNumbersWord(string):
    userList = string.split(' ')
    numbersWord = int(input("Enter numbers word string - "))
    print("Word ", str(numbersWord) + " - ", userList[numbersWord - 1] )

def printUserEnter(string):
    print("User enter string - ", string)

def exit():
    return 0

def ouputMenuConsole():
    print("_____________________________________________________")
    print("|sort the string - 1                                |")
    print("|string length - 2                                  |")
    print("|draw out vowels or consonants letter - 3           |")
    print("|break the row and draw it the other way around - 4 |")
    print("|write the word by the number - 5                   |") 
    print("|output the line again - 6                          |")
    print("|exit - 7                                           |")
    print("|---------------------------------------------------|")
def userPrograms():
    ouputMenuConsole()
    functionUser = int(input("Сhoose an action - "))
    if(functionUser == 1):
        sortUserString(inputUserString())
    elif(functionUser == 2):
        lengthUserString(inputUserString())
    elif(functionUser == 3):
        vowelsConsonantsLetters(inputUserString())
    elif(functionUser == 4):
        separationWords(inputUserString())
    elif(functionUser == 5):
        inputNumbersWord(inputUserString())
    elif(functionUser == 6):
        printUserEnter(inputUserString())
    elif(functionUser == 7):
        exit()

userPrograms()
