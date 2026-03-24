class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
       """
    
time = Time()
time.hour = 11
time.minute = 9
time.second = 30
    
def print_time(time):
    print('%.2d:%.2d:%.2d' %(time.hour, time.minute, time.second))

def is_after(t1, t2):
    t1_seconds = t1.second + t1.minute * 60 + t1.hour * 60 * 60
    t2_seconds = t2.second + t2.minute * 60 + t2.hour * 60 * 60
    while t1_seconds - t2_seconds > 0:
        return True
    return False

t1 = Time()
t1.hour = 12
t1.minute = 59
t1.second = 9

t2 = Time()
t2.hour = 11
t2.minute = 59
t2.second = 10

print(is_after(t1, t2))