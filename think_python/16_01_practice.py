class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
       """
    
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    time.minute, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(time.minute, 60)
    return time

def print_time(time):
    print('%.2d:%.2d:%.2d' %(time.hour, time.minute, time.second))

def mul_time(time, int):
   seconds = time_to_int(time)
   mutiple_seconds = seconds * int
   return int_to_time(mutiple_seconds)

def time_spend_per_mile(time, miles):
    seconds = time_to_int(time)
    time_per_mile = seconds / miles
    return int_to_time(time_per_mile)

t1 = Time()
t1.hour = 2
t1.minute = 45
t1.second = 0

t2 = Time()
t2.hour = 2
t2.minute = 98
t2.second = 0

print_time(time_spend_per_mile(t1, 10))