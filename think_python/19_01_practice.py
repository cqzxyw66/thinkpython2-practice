def binomial_coeff(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

from collections import defaultdict

def binomial_coeff_2(n, k):
    return 1 if k == 0 else (0 if n == 0 else binomial_coeff_2(n-1, k) + (binomial_coeff_2(n-1, k-1)))

print(binomial_coeff_2(4, 2))