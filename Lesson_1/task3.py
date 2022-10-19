numberOfSeconds = int(input("Enter Number seconds - "))

# There are 86400 seconds in an dey.Checking whether these seconds are day
if numberOfSeconds > 86400:
    numbers = numberOfSeconds // 86400
    print("Dey ", numbers, end="")
    
    numbers = (numberOfSeconds % 86400) // 3600
    print(" Hour ", numbers, end="")
    
    numbers = ((numberOfSeconds % 86400)% 3600)// 60
    print(" Minute ", numbers, end="")
    
    numbers = ((numberOfSeconds % 86400)% 3600)% 60
    print(" Second ", numbers)

# There are 3600 seconds in an hour.Checking whether these seconds are hour
if numberOfSeconds > 3600 and numberOfSeconds < 86400:
    numbers = numberOfSeconds // 3600
    print("Hour ", numbers, end="")
    
    numbers = (numberOfSeconds % 3600)// 60
    print(" Minute ", numbers, end="")
    
    numbers = (numberOfSeconds % 3600)% 60
    print(" Second ", numbers)

# There are 60 seconds in an minute.Checking whether these seconds are minute
if numberOfSeconds > 60 and numberOfSeconds < 3600:
    numbers = numberOfSeconds // 60
    print("Minute ", numbers, end="")
    
    numbers = numberOfSeconds % 60
    print(" Second ", numbers)
