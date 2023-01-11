import random

def makeRan():
    numlis = []
    for i in range(0,10):
        numlis.append(random.randint(1,100))
    return numlis
def callRan():
    randomInt = makeRan()
    print("The random number", randomInt)
