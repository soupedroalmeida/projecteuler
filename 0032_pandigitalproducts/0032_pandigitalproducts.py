def check_pandigital(product):
    compare_string = []
    result = []
    
    for operation in range(len(product)):
        for i in range(2):
            for c in str(product[operation][i]):
                compare_string.append(int(c))

        if len(str(product)) == 10 - len(compare_string):
            for c in str(product[operation][0] * product[operation][1]):
                compare_string.append(int(c))
            
        compare_string.sort()

        if len(compare_string) == 9:
            print(compare_string)
            
        result.append(compare_string == list(range(1, 10)))
        compare_string = []

    return result

initial_product = [[39, 186], [32, 32], [16, 16]]
print(check_pandigital(initial_product))