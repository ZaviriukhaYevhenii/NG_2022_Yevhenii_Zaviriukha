userInput = input('Enter numbers: ')

index = 0
Sum = 0

userInput = userInput.split(", ")
userInputIntegers = [int(numbers) for numbers in userInput]

print("Max element - " + str(max(userInputIntegers)))
print("Min element - " + str(min(userInputIntegers)))

while index < len(userInputIntegers):
    Sum += int(userInputIntegers[index])
    index = index + 1
print("The sum of all other elements - ", str(Sum - (max(userInputIntegers) + (min(userInputIntegers)))))
