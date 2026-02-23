import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.bk(length * n)

bob = turtle.Turtle()
bob.speed(1)
draw(bob, 10, 3)
turtle.mainloop()