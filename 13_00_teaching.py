""" 
13-5的练习题
import random

def histogram(t):
    a = dict()
    for i in t:
        a[i] = a.get(i, 0) + 1
    return a

def print_random_letter(t):
    a = histogram(t)
    sum_value = 0
    for key in a:
        sum_value += a[key]
    b = random.randint(0, sum_value -1)
    return b, t[b]

t = ['a', 'a', 'c', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a']
for i in range(20):
    print(print_random_letter(t))
 """

import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('emma.txt')

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

def print_most_common(hist):
    t = most_common(hist)
    print('The most common words are:')
    i = 0
    for freq, word in t[:10]:
        print(i, word, freq, sep='\t')
        i += 1

def subtract(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract_set(d1, d2):
    return set(d1) - set(d2)
    
words = process_file('words_origin.txt')
diff = subtract_set(hist, words)

print(subtract_set(hist, words))