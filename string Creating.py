name = "His name is J'hope"
dog = 'His dog name is "Micky"'
print(name)
print(dog)
myDog = "I don't have a dog. But if I have it's name will be \"Tain\""
print(myDog)
def FerToCel(temp):
    newTemp = 5*(temp-32)/9
    print("The F temperature", temp, "is equivalent to", newTemp,end='')
    print(" degree C")
    
def CelToFer(temp):
    newTemp = (9/5)*temp+32
    print("The C temperature", temp, "is equivalent to", newTemp, "degrees F")
