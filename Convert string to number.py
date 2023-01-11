def FerToCel():
    tempStr = input("Fahrentheit: ")
    temp = int(tempStr)
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit Tempatature", temp,"is equivalant to ", newTemp)
