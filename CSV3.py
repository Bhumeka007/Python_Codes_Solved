def write(file):
    import csv

    L = [['Name','Birthday','Spaciality'],
         ['RM','12/09','Leader'],
         ['Jin','04/12','High note vocal'],
         ['Suga','09/03','Main Rapper'],
         ['Jhope','18/02','Main Dancer'],
         ['Jimin','13/10','2nd main dancer'],
         ['V','30/12','Dep note vocal'],
         ['Jungkook','01/09','Main vocal']]
    f = open(file,'w',newline=' ')
    for item in L:
        csv.writer(f).writerow(item)
    f.close()
