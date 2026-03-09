# 函数将单词先转换为列表，然后列表排序。tuple()使其变为元组。
def word_to_tunle(word):
    a = list()
    for i in word:
        i = i.lower()
        a.append(i)
    b = sorted(a)
    c = tuple(b)
    return c

def word_paixu(word):
    a = word_to_tunle(word)
    b = dict()
    for index, zimu in enumerate(word):
        b[zimu] = index
    c = list()
    for i in a:
        c.append(b[i])
    d = dict()
    d[a] = c
    return d

def is_zhihuandui(word1, word2):
    if word_to_tunle(word1) == word_to_tunle(word2):
        a = word_paixu(word1)
        b = word_paixu(word2)
        a_tuple = word_to_tunle(word1)
        b_tuple = word_to_tunle(word2)
        a_value = a[a_tuple]
        b_value = b[b_tuple]
        length = len(a[a_tuple])
        c = 0
        for i in range(length):
            if a_value[i] != b_value[i]:
                c += 1
        if c == 2:
            return True
        else:
            return False
    else:
        return False
    
def zhihuandui_search(word1):
    fin = open('words_origin.txt')
    for i in fin:
        if is_zhihuandui(word1, i.strip()) is True:
            print(word1, 'and', i.strip(), 'is zhihuandui')

# print(is_zhihuandui('besliming', 'besmiling'))
zhihuandui_search('palest')