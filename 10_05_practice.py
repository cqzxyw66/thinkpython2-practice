def is_sorted(list):
    t = sorted(list)
    if list == t:
        return True
    else:
        return False
    
print(is_sorted(['a', 'b']))