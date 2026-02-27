import random

# print(random.randint(1, 365))

def has_duplicates(list):
    new_list = []
    for i in list:
        if i in new_list:
            return True
        else:
            new_list.append(i)
    return False
def birth_day_create(numbers):
    birth_day = []
    for i in range(numbers):
        birth_day.append(random.randint(1, 365))
    return birth_day
def has_birth_day_duplicate(list):
    new_list = []
    total = 0
    for i in list:
        if i in new_list:
            total += 1
        new_list.append(i)
    return total / 23 * 100

t = birth_day_create(30)
print(t)
print("%.2f%%" %(has_birth_day_duplicate(t)))