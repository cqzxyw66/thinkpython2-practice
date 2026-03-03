def ackermann(m, n):
    know_list = {'0:0': 1, '0:1': 2}
    string = str(m) + ',' + str(n)
    if string in know_list:
        return know_list[string]
    else: 
        if m == 0:
            result = n + 1
        elif m > 0 and n == 0:
            result = ackermann(m - 1, 1)
        elif m > 0 and n > 0:
            result = ackermann(m - 1, ackermann(m, n -1))
        know_list[string] = result
    return know_list[string]

print(ackermann(3, 4))