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

point = Point(1,2)
print(point)