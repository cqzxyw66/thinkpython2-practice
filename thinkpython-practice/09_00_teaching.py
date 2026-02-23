fin = open('words.txt')

# for line in fin:
#     if len(line) >= 20:
#         print(line)

# def has_no_e(word):
#     for i in word:
#         while i == 'e':
#             return False
#     return True

# count = 0
# has_no_e_nums = 0
# for line in fin:
#     word = line.strip()
#     count = count + 1
#     if has_no_e(word) :
#         has_no_e_nums = has_no_e_nums + 1

# percent = (has_no_e_nums / count) * 100
# print(percent)

def avoids(word, single):
    for i in single:
        if i in word:
            return False
    return True

print(avoids('competence', 'y'))