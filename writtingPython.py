def count(file):
    textF = open(file)
    wordsD = {}
    for line in textF:
        for word in line.lower().split():
            word = word.strip("'?,.!-/\"")
            if word not in wordsD:
                wordsD[word] = 0
            wordsD[word] = wordsD[word] + 1
    textF.close()
    print("List of word:")
    wordL = sorted(wordsD)
    for word in wordL:
        print(wordsD[word], word)
