# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     if letter in ('OQ'):
#         letter = letter + 'u'
#     print(letter + suffix)

# def find(word, letter, index):
#     while index < len(letter):
#         if letter[index] == word:
#             return index
#         index = index + 1
#     return - 1

# def count(word, letter, index):
#     count_nums = 0
#     while True:
#         m = find(word, letter, index)
#         if m == -1:
#             break
#         else:
#             count_nums = count_nums + 1
#         index = 0
#         letter = letter[(m + 1):]
#     return count_nums

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j -1
    return True

print(is_reverse('pots', 'stop'))