with open('data.txt', 'r') as f:
    expense_list = [int(line) for line in f.readlines()]

matched_numbers = []


def two_numbers(li):
    for i in li:
        for j in li:
            if i + j == 2020:
                if i not in matched_numbers:
                    global d
                    d = '1st'
                    return ([i, j])


def three_numbers(li):
    for i in li:
        for j in li:
            for k in li:
                if i + j + k == 2020:
                    if i not in matched_numbers:
                        global d
                        d = '2nd'
                        return ([i, j, k])


def multiply(matched):
    result = 1
    for i in matched:
        result = result * i
    return result


def printout(dimensions):
    global matched_numbers
    textfill = ''
    if dimensions == 2:
        matched_numbers.extend(two_numbers(expense_list))
        textfill = '1st'
    elif dimensions == 3:
        matched_numbers.extend(three_numbers(expense_list))
        textfill = '2nd'
    print(f'{textfill} part of problem: solution is {multiply(matched_numbers)}')
    matched_numbers = []


printout(2)
printout(3)
