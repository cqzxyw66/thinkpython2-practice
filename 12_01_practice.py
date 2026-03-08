def most_frequest(x):
    # 将x里面的字母，算出出现出现，赋值给字典j
    j = dict()
    for i in x:
        j[i] = j.get(i, 0) + 1
    # 将字典j进行反转，得到字典k
    k = dict()
    for key in j:
        val = j[key]
        if val not in k:
            k[val] = [key]
        else:
            k[val].append(key)
    # 对字典k的key进行倒序
    sorted_k = sorted(k, reverse=True)
    # 新建字符串result, result的取值就等于key(出现次数) * value(字母)
    result = str()
    for m in sorted_k:
        val_2 = sorted(k[m])
        for n in val_2:
            result += m * n
    return result

fin = open('words.txt')
for i in fin:
    words = i.strip()
    print(most_frequest(words))