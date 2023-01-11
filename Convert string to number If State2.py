def FerToCel():
    tempStr = input("Enter F: ")
    if tempStr:
        if tempStr.isdigit():
            temp = int(tempStr)
            newTemp = 5*(temp-32)/9
            print("F temperature", temp,"is equivalent to",newTemp,"C")
        else:
            print("You Forgot to enter number")
def inToF(inc):
    feet = inc//12
    exInc = inc - 12*feet
    print(inc,"inches is",feet,"feet and",exInc,"inches")
def inToF2(inc):
    feet = inc//12
    exInc = inc%12
    print(inc,"inches is",feet,"feet and",exInc,"inches")
