import datetime

NumberOfSeconds = int(input("Enter Number seconds - "))
# Using the library function, we convert seconds to date
convertNumber = datetime.datetime.fromtimestamp(NumberOfSeconds)
#the strftime() function represents the data in the specified format
print("day and time - ", convertNumber.strftime('%d:%H:%M:%S'))
