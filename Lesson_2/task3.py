enterNumber = int(input("Enter number - "))
rowNumbers = enterNumber
element = 0

while enterNumber > element:
    while rowNumbers > 0:
        print(str(rowNumbers) + " ", end="")
        rowNumbers = rowNumbers - 1
    print("")
    enterNumber -= 1
    rowNumbers = enterNumber    
