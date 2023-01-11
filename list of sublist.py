"""print(list(range(2,20,3)))
print(range(2,20,3))

print(12345678)
print(12,345,678)"""

SouthKorea = [["Seoul",73459664],["Deagu",4593585],["Busan",56486454]]
"""print(SouthKorea[0])"""
def city(state):
    print("Population         State")
    for Sitem in state:
        print(Sitem[1],"          ",Sitem[0])
def city2(Sdata):
    print("Population         State")
    for i in range(0,len(Sdata)):
        print(Sdata[i][1],"         ",Sdata[i][0])
def poeple(Sdata):
    Sum = 0
    NumState = len(Sdata)
    for i
