def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

fin = open('words_origin.txt')

def find_fanxiangdui():
    words = []
    reverse_words = []
    for i in fin:
        words.append(i.strip())
    for x in words:
        if is_palindrome(x):
            reverse_words.append(x)
    return reverse_words
        
print(find_fanxiangdui())