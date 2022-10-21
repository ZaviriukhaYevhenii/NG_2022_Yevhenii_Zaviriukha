numberOfSeconds = int(input("Enter Number seconds - "))

numbers = numberOfSeconds // 86400
print("Dey ", numbers, end="")
    
numbers = (numberOfSeconds % 86400) // 3600
print(" Hour ", numbers, end="")
    
numbers = ((numberOfSeconds % 86400)% 3600)// 60
print(" Minute ", numbers, end="")
    
numbers = ((numberOfSeconds % 86400)% 3600)% 60
print(" Second ", numbers)

   
