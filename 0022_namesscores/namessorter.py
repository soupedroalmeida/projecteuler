fhand = open('0022_namesscores/p022_names.txt', 'r')
data = fhand.read()
fhand.close()

names = data.split(',')
names.sort()

newfile = '' #open('0022_namesscores/sortednames.txt', 'w+')
for n in names:
    temp = n[1:-1]
    newfile += str(temp) + ','
newfile = newfile[:-1]

sortednames = open('0022_namesscores/sortednames.txt', 'w+')
sortednames.write(newfile)
sortednames.close()