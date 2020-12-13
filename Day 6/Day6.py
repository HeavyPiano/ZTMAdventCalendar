# the sum of the count of same letters (1 line per person) from each group separated by blank line
with open('data.txt', 'r') as f:
    test_answers = f.readlines()

groups = []
group = []
for i in test_answers:
    if i != '\n':
        i = i.strip('\n')
        group.append(list(i))
    else:
        groups.append(group)
        group = []
groups.append(group)
group = []

group_set = set()
group_setted_answers = []


def answer_or_operator():
    for i in groups:
        for j in i:
            for k in j:
                group_set.add(k)
        group_setted_answers.append(list(group_set))
        group_set.clear()


def answer_and_operator():
    for i in groups:  # each group
        i.sort(key=len)  # shortest list first
        trimmed_answer = i[0].copy()
        n = 1
        while n < len(i):
            for j in i[0]:  # test against 1st answer
                if j not in i[n]:
                    if j in trimmed_answer:
                        trimmed_answer.remove(j)
                    continue

            n += 1

        group_setted_answers.append(trimmed_answer)


def answer_length_calculator(group_answers_trimmed):
    group_set_answer_length = []
    for i in group_setted_answers:
        group_set_answer_length.append(len(i))
    total = sum(group_set_answer_length)
    return total


# part 1

answer_or_operator()
print(answer_length_calculator(group_setted_answers))

# part 2
group_setted_answers.clear()
answer_and_operator()
print(answer_length_calculator(group_setted_answers))
