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

print(t1.increment(59).hour, t1.increment(59).minute, t1.increment(59).second)