numlis = ['22','24','25','26','27','28']

"""print(numlis)
numlis.sort()
print(numlis)

print(sorted(numlis))"""

def alphaList():
    import random
    alp = ['j','h','o','p','e','r','m','i','n','s','u','g','a','v','k']
    random.seed(17)

    alphalis = []
    for i in range(0,10):
        alphalis.append(random.choice(alp))
    return alphalis
