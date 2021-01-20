from math import factorial
def possible_routes(x, y):
    return factorial(x + y) / (factorial(x) * factorial(y))

print(possible_routes(20, 20))
