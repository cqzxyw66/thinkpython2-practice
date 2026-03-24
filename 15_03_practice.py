import turtle
import math 

bob = turtle.Turtle()

class rectangle:
    """ 
    represents a rectange.
    attributes: width, height, corner 
    """

class point:
    """ 有x,y两个属性 """

class circle:
    """ 有属性center和radius """

rectangle_instance = rectangle()
rectangle_instance.point = point()
rectangle_instance.point.x = 50
rectangle_instance.point.y = 30
rectangle_instance.weight = 200.0
rectangle_instance.height = 100.0

circle_instance = circle()
circle_instance.center = point()
circle_instance.radius = 75
circle_instance.center.x = 150
circle_instance.center.y = 150

def draw_rect(turtle, rectange):
    distance = math.sqrt(rectange.point.x ** 2 + rectange.point.y ** 2)
    turtle.lt(45)
    turtle.fd(distance)
    turtle.rt(45)
    for i in range(2):
        turtle.fd(rectange.weight)
        turtle.lt(90)
        turtle.fd(rectange.height)
        turtle.lt(90)

def draw_circle(turtle, circle):
    turtle.delay = 0.01
    circle_zhouchang = math.pi * 2 * circle.radius
    circle_huchang = circle_zhouchang / 360
    hudu = math.atan(circle.center.y / (circle.center.x - circle.radius))
    jiaodu = math.degrees(hudu)
    turtle.lt(jiaodu)
    turtle.fd(math.sqrt(circle.center.y ** 2 + (circle.center.x - circle.radius) ** 2))
    turtle.rt(jiaodu)
    turtle.fd(2 * circle.radius)
    turtle.lt(90)
    for i in range(360):
        turtle.lt(1)
        turtle.fd(circle_huchang)

draw_circle(bob, circle_instance)
turtle.mainloop()