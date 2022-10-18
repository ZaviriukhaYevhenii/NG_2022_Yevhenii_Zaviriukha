firstNumber = int(input("Enter first number - "))
secondNumber = int(input("Enter second number - "))

print("=============================================")
print("Sum - 1; Multiplication - 2; Division - 3 ")
print("Subtraction - 4; Square - 5; Square root - 6")
print("=============================================")

operation = int(input("Select an operation - "))

if operation == 1:
    print("Sum = " + str(firstNumber + secondNumber))
if operation == 2:
    print("Multiplication = " + str(firstNumber * secondNumber))
if operation == 3:
    print("Division = " + str(firstNumber / secondNumber))
if operation == 4:
    print("Subtraction = " + str(firstNumber - secondNumber))   
if operation == 5:
    print("Square firstNumber = " + str(firstNumber**2))
    print("Square secondNumber = " + str(secondNumber**2))
if operation == 6:
    print("Square root firstNumber = " + str(firstNumber**0.5))
    print("Square root secondNumber = " + str(secondNumber**0.5))
