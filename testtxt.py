f = open('data.txt', 'r')
coord = f.readlines()
x = int(coord[0])
y = int(coord[1])
f.close()

print(x, y)