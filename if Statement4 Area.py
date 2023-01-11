def area(typ, x):
    if typ == "circle":
        area = 3.14*x**2
        print(area)
    elif typ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one")
