'''
recurse函数调用时，n不能小于0
'''
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(5, 7)