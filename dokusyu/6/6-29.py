import functools
data = [2, 3, 4, 5]
multi = functools.reduce(lambda result, x: result * x, data)
print(multi) #120
"""
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
"""