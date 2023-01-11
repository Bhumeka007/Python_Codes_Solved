def add():
    Sum = 0
    while True:
        num = int(input("Enter a number, input 0 to quit: "))
        if num == 0:
            break
        Sum = Sum+num
    print(Sum)
