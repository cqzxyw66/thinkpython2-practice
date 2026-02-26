def cunmsum(x):
    s = []
    length = len(x)
    for i in range(length):
        # t += sum(x[:i])
        # s.append(t)
        s.append(sum(x[:(i+1)]))
    return s

t = [1, 2, 3, 4, 5]
print(cunmsum(t))