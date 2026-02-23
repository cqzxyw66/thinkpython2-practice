def countdown(n):
    if n <= 0:
        print('0或复数')
    else:
        print(n)
        countdown(n - 1)

countdown(3)