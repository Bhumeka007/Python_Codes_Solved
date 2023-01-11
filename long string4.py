import random

def sameRealRan():
    realLis = []
    random.seed(17)
    for i in range(0,10):
        realLis.append(random.random())
    return realLis
