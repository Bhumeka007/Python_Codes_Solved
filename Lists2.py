SouthKorea = [["Seoul",1265946],["Daegu",5465445],["Busan",6549656],
              ["Gwangju",3216844],["Gwacheon",4664541],["llsan",3646545]]
def People(Sdata):
    Sum = 0
    NumState = len(Sdata)
    for i in range(0,NumState):
        OneState = Sdata[i]
        pop = OneState[1]
        Sum = Sum + pop
    print("Total Population: ",Sum)
    print("There are",NumState,"states in this list.")
def People2(Sdata):
    pop = 1
    Sum = 0
    Snum = len(Sdata)
    for state in range(0,Snum):
        Sum = Sum + Sdata[state][pop]
    print("Total population: ",Sum)
    print("There are",Snum,"states in the list.")
    
Nlis1 = [23, 24, 25, 26, 27, 28, 29]
Nlis2 = [15, 56, 89, 48, 65, 78, 23]

def ave(num):
    Sum = 0
    Tot = len(num)
    for i in range(0,Tot):
        Sum = Sum + num[i]
    A = Sum/Tot
    print("Total: ",Sum)
    print("Average: ",A)
