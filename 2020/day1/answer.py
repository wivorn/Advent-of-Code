from itertools import combinations

with open('input') as f:
    input = [int(x) for x in f.read().split('\n')]

    # Part 1
    answer1 = [x[0] * x[1] for x in list(combinations(input, 2)) if sum(x) == 2020 ][0]

    # Part 2
    answer2 = [x[0] * x[1] * x[2] for x in list(combinations(input, 3)) if sum(x) == 2020 ][0]

    print(f'Part 1: {answer1}')
    print(f'Part 2: {answer2}')
