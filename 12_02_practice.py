def word_to_tunle(word):
    a = list()
    for i in word:
        i = i.lower()
        a.append(i)
    b = sorted(a)
    c = tuple(b)
    return c

def is_huiwen(word_list):
    a = dict()
    for word in word_list:
        b = word_to_tunle(word)
        c = list()
        if b not in a:
            c.append(word)
            a[b] = c
        else:
            a[b].append(word)
    c = dict()
    for key, value in a.items():
        d = len(value)
        if d > 1:
            c[key] = a[key]
    return c

def print_sorted_huiwen(word_list):
    a_dict = is_huiwen(word_list)
    b = dict()
    for key, value in a_dict.items():
        c = len(value)
        d = list()
        if c not in b:
            d.append(tuple(value))
            b[c] = d
        else:
            b[c].append(tuple(value))
    c = list()
    for key2, value2 in b.items():
        c.append(key2)
    d = sorted(c, reverse=True)
    e = list()
    for key3 in d:
        e.append(b[key3])
    return e


# print(print_sorted_huiwen(['abc', 'cba', 'bca', 'cry', 'cyr', 'qwer', 'rewq', 'qewr', 'qrwe','iuj', 'jui']))

fin = open('words.txt')
a= list()
for i in fin:
    word = i.strip()
    a.append(word)
b = print_sorted_huiwen(a)

for i in b:
    if len(i) > 1:
        for j in i:
            print(j)
    else:
        print(i[0])