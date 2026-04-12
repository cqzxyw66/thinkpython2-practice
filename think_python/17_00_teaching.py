class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


t1 = Time()
t1.hour = 9
t1.minute = 44
t1.second = 0

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '坐标X轴为%g, Y轴为%g' % (self.x, self.y)
    
    def __add__(self, other):
        type_other = type(other)
        new_point = Point()
        if type_other is Point:
            new_point.x = self.x + other.x
            new_point.y = self.y + other.y
        elif type_other is tuple:
            new_point.x = self.x + other[0]
            new_point.y = self.y + other[1]
        return new_point
    
    def __radd__(self, other):
        return self.__add__(other)

point1 = 1, 6
point2 = Point(2,3)

print(point1 + point2)