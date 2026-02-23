def doubles_need_3(word):
    i = 0
    detection = 0
    length = len(word) - 1
    while i < length:
        if word[i] == word[(i+1)]:
            detection = detection + 1
        i = i + 1
    return detection


fin = open('words.txt')
for line in fin:
    word = line.strip()
    if doubles_need_3(word) == 3:
        print(word)
