def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def main():
    for i in range(9999):
        str_number = str(i)
        length = len(str_number)
        k = 4
        while length > 3 and k <= length:
            if is_palindrome(str_number[-k:]):
                print(i)
                break
            k = k + 1
main()