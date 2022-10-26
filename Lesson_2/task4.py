numbers = int(input("Enter a number for the factorial - "))
factorialNumbers = 1

while numbers > 0:
    factorialNumbers = factorialNumbers * numbers
    numbers = numbers - 1
print("\nFactorial - ", factorialNumbers)
