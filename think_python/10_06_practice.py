def is_anagram(parameter_list1, parameter_list2):
    a = list(parameter_list1)
    b = list(parameter_list2)
    if sorted(a) == sorted(b):
        return True
    else:
        return False
    
t1 = 'amanda'
t2 = 'daaman'

print(is_anagram(t1, t2))