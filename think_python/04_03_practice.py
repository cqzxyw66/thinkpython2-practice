import math
import turtle

bob = turtle.Turtle()
print(bob)

# def polygon(t, n, length):
#     angle = 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n 
    
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# def petal(t, r, angle):
#     for i in range(2):
#         arc(t, r, angle)
#         t.lt(180 - angle)

# def flower(t, n, r, angle):
#     for i in range(n):
#         petal(t, r, angle)
#         t.lt(360.0 / n)

# def move(t, length):
#     t.pu()
#     t.fd(length)
#     t.pd()


def sanjiao(t, r, n):
    t.delay = 0.00001
    single_angle = 360 / n
    reverse_single = 0
    two_equal_single = (180 - single_angle) / 2
    angle_raians = math.radians( two_equal_single )
    y = 2 * (r * math.cos(angle_raians))
    
    #先调转180度
    t.lt(180)
    t.fd(r)
    t.rt(180 - two_equal_single)
    t.fd(y)
    t.rt(180 - two_equal_single)
    t.fd(r)
    


def pie(t, r, n):
    for i in range(n):
        sanjiao(t, r, n)

pie(bob, 200, 3)
turtle.mainloop()