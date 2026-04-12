def str_to_list(word):
    s = []
    s.append(word)
    return(s)

def str_to_list2():
    return

file = open('words_origin.txt')

words_list = []
for i in file:
    word = i.strip()
    words_list += [word]
print(words_list)
