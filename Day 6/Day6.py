# the sum of the count of same letters (1 line per person) from each group separated by blank line
with open('data.txt', 'r') as f:
    test_answers = f.readlines()

groups = []
group = []
for i in test_answers:
    if i == '\n':
        groups.append(group)
        group = []
    else:
        i.strip('\n')
        group.append(i)

print(groups)
