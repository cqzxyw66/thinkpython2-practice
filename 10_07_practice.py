def has_duplicates(list):
    new_list = []
    for i in list:
        if i in new_list:
            return True
        else:
            new_list.append(i)
    return False
    
t = ['123', '321', '1234', '12345']
print(has_duplicates(t))