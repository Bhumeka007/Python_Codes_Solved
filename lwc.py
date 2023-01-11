filename = sys.ara[1]
text_file = open(filename)

linect = 0
wordct = 0
charct = 0
for line in text_file:
    linect = linect + 1
    for word in line.split():
        wordct = wordct + 1
    charct = charct + len(line)
text_file.close()
print(linect, wordct, charct)
