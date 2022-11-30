import os
from rich.console import Console
import platform

def convertValue(element):
    if(element == True):
        return "yes"
    else: return "no"

def printConsoleInfo():
    categories = ['CPU','OS','Architecture','User name', 'Windows version','Procced']
    saveSelection = [False,False,False,False,False]
    lentglist = int(len(categories))
    choice = 0
    console = Console()

    while(choice != 5 ):
        console.rule("[bold red] Menu")
        for element in range(lentglist):
            if(element != lentglist - 1):
                print(str(element) + ") " + categories[element] + " [" + convertValue(saveSelection[element]) + "]")
            else:
                print(str(element) +  ") " + categories[element])
        choice = int(input("Choose a category - "))
        if(choice >= 0 and choice < 5):
            if(saveSelection[choice] == False):
                saveSelection[choice] = True
            else: saveSelection[choice] = False
        else: break
        os.system('cls')

    writeFileInfo(saveSelection)

    console.rule("Stop system")

def writeFileInfo(mylist):
    for element in range(len(mylist)):
        if(mylist[element] == True):
            functionInfo(element)
        else: continue

def functionInfo(element):
    if(element == 0):
        dataFile = open("InfoSystem.txt", "a")
        fileContents = str(platform.processor())
        dataFile.write("------CPU------\n" + fileContents + "\n\n")
        dataFile.close()
    if(element == 1):
        dataFile = open("InfoSystem.txt", "a")
        fileContents = str(platform.system())
        dataFile.write("------OS------\n" + fileContents + "\n\n")
        dataFile.close()
    if(element == 2):
        dataFile = open("InfoSystem.txt", "a")
        fileContents = str(platform.architecture())
        dataFile.write("------Architecture------\n" + fileContents + "\n\n")
        dataFile.close()
    if(element == 3):
        dataFile = open("InfoSystem.txt", "a")
        fileContents = str(platform.uname())
        dataFile.write("------Name------\n" + fileContents + "\n\n")
        dataFile.close()
    if(element == 4):
        dataFile = open("InfoSystem.txt", "a")
        fileContents = str(platform.win32_ver())
        dataFile.write("------Windows version------\n" + fileContents + "\n\n")
        dataFile.close()

printConsoleInfo()