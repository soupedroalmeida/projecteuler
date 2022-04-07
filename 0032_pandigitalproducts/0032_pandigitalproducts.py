def check_pandigital(operators_list):
    compare_string = []
    result = []
    
    for operators in range(len(operators_list)):
        for i in range(2):
            for c in str(operators_list[operators][i]):
                compare_string.append(int(c))

        product = str(operators_list[operators][0] * operators_list[operators][1])

        if len(product) + len(compare_string) == 9:
            for c in product:
                compare_string.append(int(c))
            
        compare_string.sort()
        print(compare_string)
            
        result.append(compare_string == list(range(1, 10)))
        compare_string = []

    return result

initial_product = [[39, 186], [32, 32], [16, 16]]
print(check_pandigital(initial_product))