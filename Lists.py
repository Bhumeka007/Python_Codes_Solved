def who_is_there(lis):
    if "bear" in lis:
        print("There's a bear.")
    if "lion" in lis:
        print("There's a lion.")
    if "daisy" in lis or "iris" in lis:
        print("There are flowers.")
    if "daisy" in lis and "iris" in lis:
        print("There area at least two flowers.")
    if "donkey" in lis:
        print("There are a donkey.")
    if "horse" not in lis:
        print("There is no horse in the list.")
    print("The list has", len(lis), "items")

lis = ['a','b','c','d','e','f']
lis1 = ['a','b','a','j','a','h']
def count(alist):
    jk = 0
    for let in alist:
        if let == 'a':
            jk = jk+1
    print("There are",jk,"letter a's in the list")
