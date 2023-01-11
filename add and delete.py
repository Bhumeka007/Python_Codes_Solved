phones = [["jhope",'8965327'],["jimin",'0975289']]
name_pos = 0
phone_pos = 1
phone_header = ['Name', 'Phone Num']

def proper_menu_choise(which):
    if not which.isdigit():
        print("'" + which + "'need to number")
        return False
    which = int(which)
    if which < 1 or which > len(phones):
        print("'" + str(which) + "'need to number")
        return False
    return True

def delete_phone(which):
    if not proper_menu_choise(which):
        return
    which = int(which)
    del phones[which-1]
    print("Delete", which)

def edit_phone():
    print("Eiditing")

def save_phone_list():
    print("Save")

def load_phone_list():
    print("Load")

def show_phones():
    show_phone(phone_header, "")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()

def show_phone(phone, index):
    outputstr = "{0:>3} {1:<20} {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))

def creat_phone():
    print("Enter new phone number: ")
    newname = input("Enter name: ")
    newphone_num = input("Enter phone num: ")
    phone = [newname, newphone_num]
    phones.append(phone)
    print()

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
            which = input("Delete which one ?")
            print("which is", which)
            delete_phone(which)
        elif choice == 's':
            show_phone()
        elif choice == 'e':
            edit_phone()
        else:
            print("Invalid")
    save_phone_list()
