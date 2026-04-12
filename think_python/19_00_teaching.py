def use_all(word, required):
    return all(letter in required for letter in word)

print(use_all('vogce', 'vvooiicchfdfeq'))

import collections
from collections import defaultdict

