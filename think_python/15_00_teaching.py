import math
import copy

class point:
    """
    Repersents a point in 2D space. 
    """

blank = point()
blank.x = 3.0
blank.y = 4.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_point(p, q):
    length = abs(q.x - p.x)
    width = abs(q.y - q.x)
    distance = math.sqrt(length**2 + width**2)
    distance = '%g' %distance
    return distance

point1 = point()
point1.x = 3.0
point1.y = 4.0

point2 = point()
point2.x = 5.0
point2.y = 6.0

class rectangle:
    """ 
    represents a rectange.
    attributes: width, height, corner 
    """

box = rectangle()
box.width = 100.0
box.height = 200.0
box.corner = point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def move_rectangle(rect, dx, dy):
    rect.corner.x = dx
    rect.corner.y = dy
    rect.width += dx
    rect.height += dy
    return rect

def move_rectangle_new(rect, dx, dy):
    m = copy.deepcopy(rect)
    m.corner.x = dx
    m.corner.y = dy
    m.width += dx
    m.height += dy
    return m

x = move_rectangle_new(box, 100, 200)
center = find_center(x)
print_point(center)