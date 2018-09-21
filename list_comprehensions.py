from math import pi

squares = []
for x in range(10):
    squares.append(x**2)
# print(squares)


squares = list(map(lambda y: y**2, squares))
# print(squares)

squares =  [z**3 for z in range(10)]
# print(squares)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))

# print(combs)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(combs)

vec = [-4, -2, 0, 2, 4]
# print([2 * elem for elem in vec])
# print([x for x in vec if x>=0])
# print([abs(x) for x in vec])

fruits = ['    banana', '     loganberry', 'passion     fruit     ']
# print([fruit.strip() for fruit in fruits])

# print([(x, x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([z for arr in vec for z in arr])

# print([ str(round(pi, x)) for x in range(6)])

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
print([[row[i] for row in matrix] for i in range(4)])

my_set = {i for i in range(10)}
my_set = my_set.union({i for i in range(10)})
print(my_set)

d = dict(sape=4139, gudio = 4127, jack=2120)
print(d)