import math
import copy

class circle:
    """ 有属性center和radius """

class point:
    """ 有x,y两个属性 """

class rectangle:
    """ 
    represents a rectange.
    attributes: width, height, corner 
    """

circle_instance = circle()
circle_instance.center = point()
circle_instance.radius = 75
circle_instance.center.x = 150
circle_instance.center.y = 100

def point_in_circle(circle, point):
    abs_x = abs(circle.center.x - point.x)
    abs_y = abs(circle.center.y - point.y)
    distance = math.sqrt(abs_x ** 2 + abs_y ** 2)
    if distance > circle.radius:
        return False
    else:
        return True
    
point_instance = point()
point_instance.x = 224
point_instance.y = 101

print(point_in_circle(circle_instance, point_instance))