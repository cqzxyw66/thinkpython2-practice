import time

time_now = time.time()
time_seconds = int(time_now % 60)
time_minutes = int(time_now / 60 % 60)
time_hours = int(time_now / 60 / 60 % 24)
time_days = int(time_now / 60 / 60 // 24)

print( '当前时间总共秒：',time_now) 
print('已经过度过：',time_days,'天', end=' ')
print( time_hours, '小时', end=' ')
print(time_minutes, '分钟', end=' ')
print(time_seconds, '秒')