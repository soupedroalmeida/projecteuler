def square_difference(limit):
    square_sum = (((1 + limit) * limit) / 2) ** 2
    sum_square = 0
    for i in range(1, limit + 1): sum_square += i ** 2
    return square_sum - sum_square

print(square_difference(100))
