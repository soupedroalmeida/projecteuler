def palindromes(range_min, range_max):
    pali_list = list()
    for i in range(range_min, range_max + 1):
        for j in range(range_min, range_max + 1):
            if str(i * j) == str(i * j)[::-1]: pali_list.append(i * j)
    return max(pali_list)
print(palindromes(100, 999))
