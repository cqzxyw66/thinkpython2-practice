def has_duplicates(list):
    new_dict = {}
    for i in list:
        if i in new_dict:
            return True
        else:
            new_dict[i] = False
    return False
    
t = ['123', '321', '1234', '12345', '123456', '123']
print(has_duplicates(t))