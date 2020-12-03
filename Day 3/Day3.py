# set variables here

slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # x, y
height = 0
tree_count = 0
tree_total = 0


# set map height here

f = open('data.txt', 'r')
for line in f:
    height += 1

# calculate max distance needed to cover

distance = height*max(slope)[0]

# find x to search for tree


def x_coordinator(i, y):
    x = int(y * (slope[i][0]/slope[i][1]))
    return x

# feed x and current height


def tree_checker(x, reading_line):
    tree_counted = 0
    if reading_line[x] == '#':
        tree_counted = True
    return tree_counted


# generate a map in list form for current height layer being checked and run tree checker for each layer, return amount of trees detected at each layer


def map_generator(gradient):
    tree_multiplier = 0
    g = open('data.txt', 'r')
    for y, line in enumerate(g):
        reading_line = []
        lines_stripped = line.strip()
        if y % slope[i][1] == 0:
            while len(reading_line) < distance:
                reading_line.extend(lines_stripped)
            if tree_checker(x_coordinator(gradient, y), reading_line):
                tree_multiplier += 1
    return tree_multiplier


# count tree hit in each slope setting

i = 0
while i < len(slope):
    if tree_count == 0:
        tree_count = map_generator(i)
    else:
        tree_count = tree_count * int(map_generator(i))
    i += 1


print(tree_count)
