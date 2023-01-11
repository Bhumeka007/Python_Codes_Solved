def delete_phone():
    print("Delete")

def edit_phone():
    print("Eiditing")

def save_phone_list():
    print("Save")

def load_phone_list():
    print("Load")

def show_phone():
    print("Show")

def creat_phone():
    print("Creat")

def menuCho():
    print("Chose Menu: ")
    print("   s)Show")
    print("   n)New")
    print("   d)Delete")
    print("   e)Eidit")
    print("   q)Quite")
    choice = input("choice: ")
    if choice.lower() in ['n','s','d','e','q']:
        return choice.lower()
    else:
        print(choice + "?" + "Invalid")
        return None 
def main_loop():
    load_phone_list()
    while True:
        choice = menuCho()
        if choice == None:
            continue
        if choice == 'q':
            print("Exiting...")
            break
        elif choice == 'n':
            creat_phone()
        elif choice == 'd':
            delete_phone()
        elif choice == 's':
            show_phone()
        elif choice == 'e':
            edit_phone()
        else:
            print("Invalid")
    save_phone_list()

"""if _name_ == '_main_':
    main_loop()"""
