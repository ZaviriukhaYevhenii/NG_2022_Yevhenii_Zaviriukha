string = input("Enter sting: ")
index = 0
letter = ""
sortList = []
letterCount = []

alphabet = ["A","a","B","b","C","c","D","d","E","e","F","f",
            "G","g","H","h","I","i","J","j","K","k","L","l",
            "M","m","N","n","O","o","P","p","Q","q","R","r",
            "S","s","T","t","U","u","V","v","W","w","X","x",
            "Y","y","Z","z"]

while index < len(alphabet):
    letter = string.count(alphabet[index])
    letterCount.insert(index, letter)
    index += 1

index = 0
print("\nI deduce the number by the letters themselves\n")

while index < len(alphabet):
    print(str(alphabet[index]) + " - " + str(letterCount[index]) + ", ", end="")
    index += 1

index = 0
print("\n\n=======================================================\n")

while index < len(alphabet):
    if(letterCount[index] > 0):
        print(str(alphabet[index]) + " - " + str(letterCount[index])+ ", ", end="")
        sortList.append(letterCount[index])
    index += 1
    
sortList.sort(reverse = True)
print("\nSort - ", sortList)
