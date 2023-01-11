def FerToCel():
    tempStr = input("Enter F: ")
    if tempStr:
        temp = int(tempStr)
        newTemp = 5*(temp-32)/9
        print("The Fahrenheit temperature", temp, "is equivalent to",newTemp)
