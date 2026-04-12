

def middle(a, b, c):
    global middle_num
    if a > b > c or a < b < c:
        middle_num = b 
    elif a > c > b or a < c < b:
        middle_num = c
    else:
        middle_num =a

a = int(input('请输入边长：'))
b = int(input('请输入边长：'))
c = int(input('请输入边长：'))

def is_triangle(a, b, c):
    # max_num = max(a, b, c)
    # min_num = min(a, b, c)
    # if a > b > c or a < b < c:
    #     middle_num = b 
    # elif a > c > b or a < c < b:
    #     middle_num = c
    # else:
    #     middle_num =a
    middle(a, b, c)
    
    if min(a, b, c) + middle_num >= max(a, b, c):
        print('可以组成三角形')
    else:
        print('不能组三角形')

is_triangle(a, b, c)