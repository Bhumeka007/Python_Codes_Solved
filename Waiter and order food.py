def dinner():
    print("Hello, I'll be your waitress. What will you have?")
    print()
    menu = []
    while True:
        Formenu = input("menu item: ")
        if Formenu == "that's all":
            break
        menu.append(Formenu)
    print(menu)
