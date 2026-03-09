# 函数将单词先转换为列表，然后列表排序。tuple()使其变为元组。
def word_to_tunle(word):
    a = list()
    for i in word:
        i = i.lower()
        a.append(i)
    b = sorted(a)
    c = tuple(b)
    return c

#函数为输入一个列表，输出单词中字母排序先作为key，value为单词。而且只挑选出现过两次的单词，1次的不会列入。
def is_huiwen(word_list):
    # 新增字典a
    a = dict()
    # 遍历输入的列表
    for word in word_list:
        b = word_to_tunle(word)
        c = list()
        # 当该单词出现（意味着本单词在列表中，而没有出现在已有的列表中）
        # 时，key为字母顺序元组，value为本单词。
        if b not in a:
            c.append(word)
            a[b] = c
        # 如果发现单词的字母顺序元组key出现过，就将value增加一个本单词
        else:
            a[b].append(word)
    # 定义一个新字典c，c字典用来剔除那些值只有1的key-values
    c = dict()
    for key, value in a.items():
        d = len(value)
        # 判断当值，如果键值对中的值，就是单词数量多于1个时。就能判断此单词有回文兄弟。
        # 就加入进字典c
        if d > 1:
            c[key] = a[key]
    return c

# 按照顺序进行对回文单词进行由多到少的打印，函数需要传入列表
def print_sorted_huiwen(word_list):
    # 先将传入的参数，用is_huiwen函数，返回key为字母顺序，value为单词的字典。而且值是要多于1的。
    # 1个的不要来~
    a_dict = is_huiwen(word_list)
    b = dict()
    # 对字典a进行遍历
    for key, value in a_dict.items():
        c = len(value)
        d = list()
        # 主要将键值对进行反转，key为单词的数量，value为单词列表。
        # 比如{2:[('abc', 'cba'), ('try', 'yrt')]}
        if c not in b:
            d.append(tuple(value))
            b[c] = d
        else:
            b[c].append(tuple(value))
    # 新建列表c，主要是将key收集起来，进行排序
    c = list()
    for key2, value2 in b.items():
        c.append(key2)
    d = sorted(c, reverse=True)
    # 新建列表e，将c里面（已经是从大到小排序的值3、2、1），然后取得字典b里面的b[key]的单词列表
    e = list()
    for key3 in d:
        e.append(b[key3])
    return e


# print(print_sorted_huiwen(['abc', 'cba', 'bca', 'cry', 'cyr', 'qwer', 'rewq', 'qewr', 'qrwe','iuj', 'jui']))

fin = open('words.txt')
a= list()
for i in fin:
    word = i.strip()
    a.append(word)
b = print_sorted_huiwen(a)

for i in b:
    if len(i) > 1:
        for j in i:
            print(j)
    else:
        print(i[0])