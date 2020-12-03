# set variables here

slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # x, y
tree_count = 0
tree_total = 0


# set map height and width here

f = open('data.txt', 'r')
map = f.readlines()
map_width = len(map[0]) - 1
del f

# find x to search for tree


def x_coordinator(i, y):
    x = int(y * (slope[i][0]/slope[i][1]))
    looped_x = x % map_width
    return looped_x

# feed x and current height


def tree_checker(x, reading_line):
    tree_counted = 0
    if reading_line[x] == '#':
        tree_counted = True
    return tree_counted


# generate a map in list form for current height layer being checked and run tree checker for each layer, return amount of trees detected at each layer


def map_generator(gradient):
    tree_multiplier = 0
    for y, line in enumerate(map):
        if y % slope[i][1] == 0:
            if tree_checker(x_coordinator(gradient, y), line.strip()):
                tree_multiplier += 1
    return tree_multiplier


# count tree hit in each slope setting

i = 0
while i < len(slope):
    if tree_count == 0:
        tree_count = map_generator(i)
    else:
        tree_count *= map_generator(i)
    i += 1


print(tree_count)
