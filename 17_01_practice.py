class Time:
    def __init__(self, seconds = 0):
        self.second = seconds
    
    def int_to_time(self):
        minutes, self.second = divmod(self.second, 60)
        self.hour, self.minute = divmod(minutes, 60)
        return self
    
    def __str__(self):
        self.int_to_time()
        return '转化为时间格式是%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

a = Time(6543)
print(a)