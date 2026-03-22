import anagram_sets

# huiwen = anagram_sets.huiwen('words.txt')
# a = dict()
# for i in huiwen:
#     length = len(i)
#     for j in range(length):
#         line = i[j]
#         length_line = len(line)
#         first_word_in_line = ''.join(sorted(line[0]))
#         new_list = list()
#         for key in line:
#             new_list.append(key)
#         key_2 = first_word_in_line, length_line
#         a[key_2] = new_list

def store_anagrams(origin_filename, destination_filename, writable='y'):
    huiwen = anagram_sets.huiwen(origin_filename)
    if writable == 'y':
        fp = open(destination_filename, 'w')
    a = dict()
    for i in huiwen:
        length = len(i)
        for j in range(length):
            line = i[j]
            length_line = len(line)
            first_word_in_line = ''.join(sorted(line[0]))
            new_list = list()
            for key in line:
                new_list.append(key)
            key_2 = first_word_in_line # 也可以加上', length_line作为回文数量，这里就没加了'
            a[key_2] = new_list
            if writable == 'y':
                fp.write(f'{key_2}, {length_line}:{new_list}\n')
    return a
sortd_letters = store_anagrams('words_origin.txt', 'new_file.txt', writable = 'n')

def read_anagrams(word, file='words_origin.txt'):
    a_sorted = ''.join(sorted(word))
    try:
        print(sortd_letters[a_sorted])
    except:
        print('不存在回文的哈，兄弟')

read_anagrams('deist')