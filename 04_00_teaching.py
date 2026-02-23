import turtle
import math

bob = turtle.Turtle()
bob.delay = 0.01
print(bob)

# for i in range(50):
#     bob.fd(100)
#     bob.lt(80)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def square2(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r ):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n 
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 10, 355)
turtle.mainloop()