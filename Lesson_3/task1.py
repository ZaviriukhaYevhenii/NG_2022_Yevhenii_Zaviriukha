def inputFirstNumber():
    firstNumbers = int(input("\nEnter one numbers - "))
    return firstNumbers

def inputSecondNumber():
    secondNumbers = int(input("Enter two numbers - "))
    return secondNumbers

def printConsole():
    print("=============================================")
    print("Sum - 1; Multiplication - 2; Division - 3 ")
    print("Subtraction - 4; Square - 5; Square root - 6")
    print("=============================================")

def Sum(number, number2):
    print("Sum - " + str(number + number2))

def Subtraction(number, number2):
    print("Subtraction - " + str(number - number2))

def Multiplication(number, number2):
    print("Multiplication - " + str(number * number2))

def Division(number, number2):
    print("Division - " + str(number / number2))

def Square(number, number2):
    print("Square firstNumber - " + str(number ** 2))
    print("Square secondNumber - " + str(number2 ** 2))

def squareRoot(number, number2):
     print("Square root firstNumber - " + str(number ** 0.5))
     print("Square root secondNumber - " + str(number2 ** 0.5))

def Calculator():
    printConsole()
    operation = int(input("Select an operation - "))
    if operation == 1:
        Sum(inputFirstNumber(), inputSecondNumber())
    if operation == 2:
        Multiplication(inputFirstNumber(), inputSecondNumber())
    if operation == 3:
        Division(inputFirstNumber(), inputSecondNumber())
    if operation == 4:
        Subtraction(inputFirstNumber(), inputSecondNumber())
    if operation == 5:
        squareRoot(inputFirstNumber(), inputSecondNumber())
    if operation == 6:
        squareRoot(inputFirstNumber(), inputSecondNumber())

Calculator()
