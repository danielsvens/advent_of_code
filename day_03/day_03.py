from collections import OrderedDict

""" NOTES """

input_dict = OrderedDict()

with open('input_data.txt', 'r') as f:
    for line in f.readlines():
        input_dict.update({line.split()[0][1:]: [tuple(line.split()[2][:-1].split(',')), tuple(line.split()[3].split('x'))]})

print(input_dict['1'])
print(input_dict['1'][0])
print(input_dict['1'][1])

# Part One
grid = [['.'] * 8 for _ in range(8)]

"""
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""
l, r = 1, 3

# Prototyp
data = {'1': [(1, 3), (4, 4)]}  # ID - tuple kordinater - tuple area

for _ in range(4):
    grid[l][r:r + 4] = '#' * 4
    l += 1

l = 1
for _ in range(4):
    grid[r][l:l + 4] = '#' * 4
    r += 1

print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])

# Output
""" 
['.', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '#', '#', '#', '#', '.']
['.', '.', '.', '#', '#', '#', '#', '.']
['.', '#', '#', '#', '#', '#', '#', '.']
['.', '#', '#', '#', '#', '#', '#', '.']
['.', '#', '#', '#', '#', '.', '.', '.']
['.', '#', '#', '#', '#', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', '.']
"""
