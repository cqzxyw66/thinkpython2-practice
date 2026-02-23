def detect_word_length(word):
    if len(word) >= 4:
        return True
    
def is_reversible(word):
    i = 0
    j = len(word) - 1
    new_word = str(word)
    while i < j:
        if new_word[i] == new_word[j]:
            return True
        i = i + 1
        j = j - 1