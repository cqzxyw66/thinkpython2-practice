import math

def test_square_root(a):
    x = 0.0
    epsilon = 0.1
    print("{:<10} {:<20} {:<20} {:<20}".format("a", "mysqrt(a)", "math.sqrt(a)", "diff"))
    while x < 100:
        x = x + 0.1
        y = (x + a/x) / 2
        math_sqrt = math.sqrt(x)
        diff = y - x
        if abs(y -x) < epsilon:
            x = y
            break
        print("{:<10} {:<20} {:<20} {:<20}".format(x, y, math_sqrt, diff))
    print("{:<10} {:<20} {:<20} {:<20}".format(x, y, math_sqrt, diff))

test_square_root(36)