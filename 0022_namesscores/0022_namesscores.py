fhand = open('0022_namesscores/sortednames.txt', 'r')
data = fhand.read()
namelist = data.split(',')
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_score(name):
    score = 0
    for char in name:
        score += alph.index(char) + 1
    return score

result = 0
for n in namelist:
    result += get_score(n) * (namelist.index(n) + 1)

print(result)