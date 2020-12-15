input = [6, 19, 0, 5, 7, 13, 1]


def find(data, final_turn):
    current_turn = 0
    prev_value = 0
    value = 0

    last_index = {}

    while True:
        if current_turn < len(data):
            value = data[current_turn]
        elif prev_value not in last_index:
            value = 0
        else:
            value = (current_turn - 1) - last_index[prev_value]

        last_index[prev_value] = current_turn - 1

        current_turn += 1
        prev_value = value

        if current_turn == final_turn:
            break

    return value


print(f'Part1: {find(input, 2020)}')
print(f'Part2: {find(input, 30000000)}')
