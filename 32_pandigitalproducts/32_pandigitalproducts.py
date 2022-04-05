def check_pandigital(product):
    compare_string = []
    result = []
    
    for i in range(len(product)):
        for j in range(2):
            for c in str(product[i][j]):
                compare_string.append(int(c))

        for c in str(product[i][0] * product[i][1]):
            compare_string.append(int(c))
        
        if len(compare_string) == 9:
            print(compare_string)
            
        result.append(sorted(compare_string) == list(range(1, 10)))
        compare_string = []

    return result

initial_product = [[39, 186], [32, 32], [16, 16]]
print(check_pandigital(initial_product))