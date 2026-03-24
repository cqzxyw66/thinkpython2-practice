import math

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
circle_instance.center.x = 2500
circle_instance.center.y = 1000

rectangle_instance = rectangle()
rectangle_instance.point = point()
rectangle_instance.point.x = 0.0
rectangle_instance.point.y = 0.0
rectangle_instance.weight = 100.0
rectangle_instance.height = 200.0

def rect_in_circle(circle, rectange):
    max_rect_x = rectange.point.x + rectange.weight
    max_rect_y = rectange.point.y + rectange.height
    nearest_circle_x = max(min(max_rect_x, circle.center.x), rectange.point.x)
    nearest_circle_y = max(min(max_rect_y, circle.center.y), rectange.point.y)
    distance = math.sqrt((abs(circle.center.x - nearest_circle_x)) ** 2 + (abs(circle.center.y - nearest_circle_y) ** 2))
    if distance <= circle.radius:
        return True
    else:
        return False

print(rect_in_circle(circle_instance, rectangle_instance))