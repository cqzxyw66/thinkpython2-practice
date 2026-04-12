# def compare(x, y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1
    
# print(compare(-100, 1))
# import math

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquard = dx ** 2 + dy ** 2
#     result = math.sqrt(dsquard)
#     return(result)

# import math

# def hypotenuse(x, y):
#     square = x ** 2 + y ** 2
#     result = int(math.sqrt(square))
#     return result

# print(hypotenuse(3, 4))

# def circle(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     area = math.pi * (radius ** 2)
#     return area

# def is_between(x, y, z):
#     return x <= y <= z

# print(is_between(1, 3, 1))

# def jie_cheng(x):
#     if x == 0:
#         return 1
#     elif x == 1:
#         return 1
#     else: 
#         return x * jie_cheng(x - 1)

# print(jie_cheng(5))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(1.5))

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n -1)
        result = n * recurse
        print(space, 'returning', result)
        return result
    
factorial(5)