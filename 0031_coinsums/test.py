from itertools import combinations

a = [1, 1, 1, 2, 5]
result = dict()
for i in list(combinations(a, 3)):
    result[i] = None
for i in result: print(i)