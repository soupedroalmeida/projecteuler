def get_triangle_num(index):
    triangle_num = 0
    num = 1
    while num <= index:
        triangle_num += num
        num += 1
    return triangle_num

def get_divisors_num(n):
    i = 1
    count = 0
    while i ** 2 <= n: 
        if n % i == 0: 
            if n / i == i: count += 1 
            else: count += 2
        i += 1
    return count

divisors = 0
index_count = 1
while divisors < 500:
    divisors = get_divisors_num(get_triangle_num(index_count))
    index_count += 1

print(get_triangle_num(index_count - 1))
