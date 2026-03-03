fin = open('words_origin.txt')

def read_words_in_dict(t):
    dicts = dict()
    for word in fin:
        perfect_word = word.strip()
        dicts[perfect_word] = 0
    if t in dicts:
        return True
    else:
        return False

print(read_words_in_dict('spider'))