import os.path

input_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), '../../input/day1')


def totalFuelForModule(mass):
    total = 0
    while mass > 0:
        mass = mass // 3 - 2
        if mass > 0:
            total += mass

    return total


with open(input_path) as f:
    input = [int(x) for x in f.read().strip().split('\n')]

    print(f'Part 1: {sum([x // 3 - 2 for x in input])}')
    print(f'Part 2: {sum([totalFuelForModule(x) for x in input])}')
