import math

def eval_loop():
    while True:
        x = input('请输入你要求的值，直到输入done：')  
        if x == 'done':
            break
        else:
            y = eval(x)
            print(x, '计算为：', y)

eval_loop()