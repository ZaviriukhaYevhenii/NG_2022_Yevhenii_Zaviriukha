userInput = input('Enter numbers: ')

userInput = userInput.split(", ")
userInputIntegers = [int(numbers) for numbers in userInput]

print("Max element - " + str(max(userInputIntegers)))
print("Min element - " + str(min(userInputIntegers)))

print("The sum of all other elements - ", str(sum(userInputIntegers) - (max(userInputIntegers) + (min(userInputIntegers)))))
