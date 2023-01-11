"""baseball = []
baseball.append("ball")
baseball.append("bat")
baseball.append("mitt")
baseball"""
def store():
    num = []
    while True:
        Nextnum = int(input("Enter number, 0 for quit: "))
        if Nextnum == 0:
            break
        num.append(Nextnum)
    print(num)
