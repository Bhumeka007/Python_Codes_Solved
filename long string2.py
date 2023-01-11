import random
def sameRan():
    numLis = []
    random.seed(17)
    for i in range(0,10):
        numLis.append(random.randint(1,100))
    return numLis
def callRan():
    randomInt = sameRan()
    print(randomInt)
    randomInt1 = sameRan()
    print(randomInt1)
