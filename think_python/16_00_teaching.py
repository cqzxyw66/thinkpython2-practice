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

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def increment(time, seconds):
    new_time = Time()
    total_seconds = time.hour * 60 * 60 + time.minute * 60 + time.second + seconds
    new_time.hour = total_seconds // 3600
    new_time.minute = (total_seconds % 3600) // 60
    new_time.second = total_seconds % 60
    return new_time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment_new(time, seconds):
    seconds = time_to_int(time) + time_to_int(seconds)
    new_time = int_to_time(seconds)
    return new_time

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time_new(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

t1 = Time()
t1.hour = 9
t1.minute = 45
t1.second = 0

t2 = Time()
t2.hour = 2
t2.minute = 98
t2.second = 0

print_time(add_time_new(t1, t2))