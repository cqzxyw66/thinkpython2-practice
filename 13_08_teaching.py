import string
import random

def line_to_word(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist.append(word)

def file_convert_word(filename):
    hist = list()
    fp = open(filename)
    for line in fp:
        line_to_word(line, hist)
    return hist

def random_words(filename, interval=2):
    a = file_convert_word(filename)
    b = 0
    c = len(a) - interval
    d = dict()
    for i in range(c):
        new_b = b + interval
        new_key = tuple(a[b: new_b])
        new_value = a[(new_b)]
        new_list = list()
        if new_key not in d:
            new_list.append(new_value)
            d[new_key] = new_list
        else:
            d[new_key].append(new_value)
        b += 1
    return d

# t = random_words('emma.txt', 2)
# print(t[('this', 'was')])

def random_out(filename, interval=2, repeat=1):
    t = random_words(filename, interval)
    a_key = list()
    for key, value in t.items():
        a_key.append(key)
    length = len(a_key)
    random_number = random.randint(0, length)

    new_string = list()
    for i in a_key[random_number]:
        new_string.append(i)
    for i in range(repeat):
        new_key = tuple(new_string[-(interval):])
        value = random.choice(t[new_key])
        new_string.append(value)
    return ' '.join(new_string)

print(random_out('emma.txt', interval=2, repeat=20))