def nested_sum(x):
    length = len(x)
    total = 0
    for i in x:
        if type(i) is list:
            total += sum(i)
        else:
            print('你的列表不全是list，请确认')
            return False
    return total

t = [[1, 2], [3], [4, 5, 6], [7, 8, 9, 10]]
print(nested_sum(t))