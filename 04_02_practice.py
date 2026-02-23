import math
import turtle

bob = turtle.Turtle()
print(bob)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n 
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

flower(bob, 12, 100.0, 60.0)
turtle.mainloop()