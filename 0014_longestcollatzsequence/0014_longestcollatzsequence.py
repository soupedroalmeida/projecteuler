def Collatz_length(giv_range):
    len_list = list()
    for n in range(giv_range + 1):
        temp_count = 0
        temp_n = n
        finished = False
        while temp_n > 1:
            if temp_n < n:
                len_list.append(temp_count + len_list[int(temp_n)])
                finished = True
                break
            if temp_n % 2 == 0:
                temp_n /= 2
                temp_count += 1
                continue
            temp_n = temp_n * 3 + 1
            temp_count += 1
        if not finished: len_list.append(temp_count + 1)
    return len_list

result = Collatz_length(1000000)
print(result.index(max(result)))
