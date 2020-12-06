# 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7

with open('data.txt', 'r') as f:
    tickets_data = f.readlines()
tickets_stack = []
for ticket in tickets_data:
    tickets_stack.append(ticket.strip())

max_row = 127
max_column = 7

tickets_coordinates = []
seat_ids = []


def row_calculator(ticket):
    default_row_range = [0, 127]
    column = default_row_range.copy()
    for i, direction in enumerate(ticket):
        if i == 6:
            if direction == 'F':
                return column[0]
            elif direction == 'B':
                return column[1]
        elif direction == 'F':
            column[1] = column[1] - (default_row_range[1]+1)/(2**(i+1))
        elif direction == 'B':
            column[0] = column[0] + (default_row_range[1]+1)/(2**(i+1))


def column_calculator(ticket):
    default_column_range = [0, 7]
    column = default_column_range.copy()
    for i, direction in enumerate(ticket):
        if i == 2:
            if direction == 'L':
                return column[0]
            elif direction == 'R':
                return column[1]
        elif direction == 'L':
            column[1] = column[1] - (default_column_range[1]+1)/(2**(i+1))
        elif direction == 'R':
            column[0] = column[0] + (default_column_range[1]+1)/(2**(i+1))


def logic(ticket):
    row = row_calculator(ticket[:7])
    column = column_calculator(ticket[7:])
    return int(row), int(column)


for i in tickets_stack:
    seat = logic(i)
    tickets_coordinates.append(seat)
    seat_ids.append(seat[0]*8 + seat[1])

seat_ids.sort()

i = 0
while i < len(seat_ids):
    if seat_ids[i+1] - seat_ids[i] != 1:
        print(seat_ids[i])
    i += 1


# print(max(seat_ids))
