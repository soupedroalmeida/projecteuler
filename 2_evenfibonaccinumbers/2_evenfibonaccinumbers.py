# My first solution
def fib(lim):
    x = 1
    y = 2
    result = [1, 2]
    while True:
        result.append(x + y)
        x = result[-2]
        y = result[-1]
        if result[-1] > lim: 
            result.pop()
            break 
    even_result = 0
    for i in result:
        if i % 2 == 0: even_result += i
    return result, even_result
print(fib(4000000))

# AlexeiIvanovich's solution
def AlexeiIvanovich():
    a = 1
    b = 2
    total = 0

    while(a <= 4000000):
        if a % 2 == 0:
            total += a
        a, b = b, (a + b)
    print(total)
# AlexeiIvanovich()
