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