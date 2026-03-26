import datetime

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

def day_of_week():
    today = datetime.datetime.now()
    week_day = today.isoweekday()
    return print('今天是星期%d' %week_day)

def int_to_date(birthday):
    year, month, day = int(str(birthday)[0:4]), int(str(birthday)[4:6]), int(str(birthday)[6:9])
    return datetime.date(year, month, day)

def print_age(birthday):
    birth_date = int_to_date(birthday)
    today_date = datetime.date.today()
    date_gap = today_date - birth_date
    age = date_gap.days // 365
    next_birth_day = 365 - date_gap.days % 365
    # next_birthday_gap = datetime.date(,next_birth_day // 30, next_birth_day % 30)
    print('你现在已经%d岁，距离生日还有%d天'%(age, next_birth_day))
    

print_age(19880410)