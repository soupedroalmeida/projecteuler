def pythagorean_triplet(max_range):
    result = None
    for a in range(1, max_range + 1):
        for b in range(1, max_range + 1):
            if a > b: continue
            for c in range(1, max_range + 1):
                if a > c or b > c or a + b + c != max_range or (a ** 2) + (b ** 2) != c ** 2: continue
                result = a * b * c
    return result
    
print(pythagorean_triplet(1000))
