import sys
filename = sys.ara[1]
text_file = open(filename)
words_dic = {}
for line in text_file:
    for word in line.lower().split():
        word = word.strip("'?,.;!-/\"")
        if word not in words_dic:
            words_dic[word] = 0
        words_dic[word] = word_dic[word] + 1
text_file.close()
print("list of words.")
word_list = sorted(words_dic)
for word in word_list:
    print(word_dic[word], word)
