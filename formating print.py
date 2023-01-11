nam1 = "Jhope"
nam2 = "Jungkook"
age = 26
wt = 56.788976

out1 = "name: {0} age: {1} weight: {2}"
print("name: {0} age: {1} weight: {2}".format(nam1,age,wt))
print("name: {0} age: {1} weight: {2}".format(nam2,age,wt))

out2 = "name: {0:>26} age: {1:>4} weight: {2:>10}"
print("name: {0:>26} age: {1:>4} weight: {2:>10}".format(nam1,age,wt))
print("name: {0:>26} age: {1:>4} weight: {2:>10}".format(nam2,age,wt))

out3 = "name: {0:>26} age: {1:>4} weight: {2:>5.2f}"
print("name: {0:>26} age: {1:>4} weight: {2:>5.2f}".format(nam1,age,wt))
print("name: {0:>26} age: {1:>4} weight: {2:>5.2f}".format(nam2,age,wt))

print(out3.format(nam1,age,wt))
print(out3.format(nam2,age,wt))
