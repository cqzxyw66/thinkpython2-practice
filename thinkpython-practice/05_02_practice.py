def check_fermat(a, b, c, n):
    m = a**n + b**n
    n = c ** n
    if n >= 2 and m==n:
        print('天哪，费马弄错了')
    else:
        print('不，那样不行，费马还是有道理的！')
        
a = int(input('请输入整数a：'))
b = int(input('请输入整数b：'))
c = int(input('请输入整数c：'))
n = int(input('请输入指数n：'))

check_fermat(a, b, c, n)