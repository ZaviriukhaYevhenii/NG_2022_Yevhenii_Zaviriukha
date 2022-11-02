enterString = str(input("Enter string - "))
decryptedString = ""
numberOffset = int(input("\nEnter Numbers - "))
index = 0
indexLetters = 0
numberletters = 0
punctuation = 0
# list of punctuation
symbols = [".",","," ","!","\'","\"","-",":","_"]
# list of letters
alphabet = ["A","a","B","b","C","c","D","d","E","e","F","f",
            "G","g","H","h","I","i","J","j","K","k","L","l",
            "M","m","N","n","O","o","P","p","Q","q","R","r",
            "S","s","T","t","U","u","V","v","W","w","X","x",
            "Y","y","Z","z"]


while index < len(enterString):
    # Determines the letter, makes 
    # shifts and writes to the string
    while indexLetters < len(alphabet): 
        # Defines a letter
        if(enterString[index] == alphabet[indexLetters]):
            # Defines shifts
            numberletters = indexLetters + (numberOffset * 2)
            # if the shift is greater than an alphabet, 
            # then we return to the beginning
            if(numberletters >= 52):
                numberletters = numberletters - 52
            # Add the decoded letter
            decryptedString += str(alphabet[numberletters])
            break
        indexLetters += 1
    # Defines a punctuation mark and writes to a string
    while(punctuation < len(symbols)):

         if(enterString[index] == symbols[punctuation]):
            # Add the decoded letter
            decryptedString += enterString[index]
         punctuation += 1
    index += 1
    indexLetters = 0
    punctuation = 0
print("\ndeciphered text - " + decryptedString)
input()
