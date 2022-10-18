numberOne = int(input("Enter number a - "))
numberTwo = int(input("Enter number b - "))
numberThree = int(input("Enter number c - "))
rootEquationX1 = 0.0
rootEquationX2 = 0.0

discriminator = numberTwo**2 - 4 * numberOne * numberThree

if discriminator > 0:
    rootEquationX1 = (-numberTwo + numberTwo**0.5) / (2 * numberOne)
    rootEquationX2 = (-numberTwo - numberTwo**0.5) / (2 * numberOne)
    print("the root of the quadratic equation x1 - ", str(rootEquationX1))
    print("the root of the quadratic equation x2 - ", str(rootEquationX2))
if discriminator == 0:
    rootEquationX1 = -(numberTwo / (2 * numberOne))
    print("the root of the quadratic equation x1 - ", str(rootEquationX1))
if discriminator < 0:
    print("there are no real roots in the equation")
