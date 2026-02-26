def chop(list):
    # del list[0]
    # del list[-1]
    list.pop(0) and list.pop(-1)
    print(list)

t = [1, 2, 3, 4, 8, 9]
chop(t)
print(t)