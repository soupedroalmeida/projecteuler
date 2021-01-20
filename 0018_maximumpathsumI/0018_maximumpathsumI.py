thand = open('triangle.txt', 'r')

# create the triangle and assign it to the variable 'triangle' in a list of lists format
triangle = list()
for row in thand: 
    row = row.rstrip().split(' ')
    count = 0
    for num in row:
        row[count] = int(num)
        count += 1
    triangle.append(row)

# find the best route for a given element by its position
best_routes = {(0, 0) : 75, (1, 0) : 170, (1, 1) : 139}
def best_route(element):
    if element[1] == 0: best_routes[element] = triangle[element[0]][element[1]] + best_routes[(element[0] - 1, element[1])]
    elif element[1] == len(triangle[element[0]]) - 1: best_routes[element] = triangle[element[0]][element[1]] + best_routes[(element[0] - 1, element[1] - 1)]
    else: best_routes[element] = max(best_routes[(element[0] - 1, element[1])], best_routes[(element[0] - 1, element[1] - 1)]) + triangle[element[0]][element[1]]

# modify best_routes to get the best route for every element
for n1 in range(2, 15):
    count = 0
    for i in triangle[n1]:
        best_route((n1, count))
        count += 1

# assign the maximum value of best_routes to the variable 'result'
result = 0
for k in best_routes:
    if best_routes[k] > result: result = best_routes[k]

# print the result
print(result)
