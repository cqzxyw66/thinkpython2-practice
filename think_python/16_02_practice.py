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

def int_to_date(birthday) -> datetime.date:
    year, month, day = int(str(birthday)[0:4]), int(str(birthday)[4:6]), int(str(birthday)[6:9])
    return datetime.date(year, month, day)

def print_age(birthday):
    birth_date = int_to_date(birthday)
    today = datetime.date.today()
    gap = today - birth_date
    age = gap.days // 365
    this_year_birthday = datetime.date(year=today.year, month=birth_date.month, day = birth_date.day)
    if today < this_year_birthday:
        age -= 1
        next_birthday = this_year_birthday 
    else:
        next_birthday = datetime.date(year=today.year + 1, month=birth_date.month, day=birth_date.day)
    gap_next_birthday = next_birthday - today
    seconds = gap_next_birthday.seconds % 60
    minutes = seconds % 60 
    hours = minutes % 60
    # print(type(gap_next_birthday.days))

    print('你当前%d岁，距离下一个生日还有%d天,%d小时,%d分钟,%d秒' % (age, gap_next_birthday.days, hours, minutes, seconds))

def multiple_age(birthday1, birthday2, multiple=2):
    birthday1 = int_to_date(birthday1)
    birthday2 = int_to_date(birthday2)
    if birthday1 > birthday2:
        older_boy, younger_boy = birthday2, birthday1
    else:
        older_boy, younger_boy = birthday1, birthday2

    dedicated_timedetla = (multiple * (younger_boy - older_boy)) / (multiple - 1) #核心公式
    dedicated_day = older_boy + dedicated_timedetla #计算特定的日期
    older_boy_age = (dedicated_day - older_boy).days // 365
    younger_boy_age = (dedicated_day - younger_boy).days // 365
    # # print(multiple_date)
    print('下次是你%d倍的日子是%d年%d月%d日, 那时候一个%d岁%d天(共计%d天)，一个%d岁%d天(共计%d天)' % (multiple, dedicated_day.year, dedicated_day.month, dedicated_day.day, older_boy_age, (dedicated_day - older_boy).days % 365, (dedicated_day - older_boy).days,  younger_boy_age, (dedicated_day - younger_boy).days % 365, (dedicated_day - younger_boy).days))

multiple_age(19640318, 20191106, 10)