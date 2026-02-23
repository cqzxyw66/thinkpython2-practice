def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1: -1]

def reverse(word):
    length = len(word)
    if length == 1:
        return last(reverse(word[0: length -1]))

def is_palindrome(x):
    reverse_word = first(x) + middle(x) + last(x)
    return x == reverse_word

reverse('spider')