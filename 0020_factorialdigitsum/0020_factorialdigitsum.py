num = 1
for n in reversed(range(1, 101)):
    num *= n

result = 0
for c in str(num):
    result += int(c)

print(result)