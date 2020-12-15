import os.path

input_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), '../../input/day13')


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


with open(input_path) as f:
    input = f.read().strip().split('\n')

    start_time = int(input[0])
    ids = [int(i) for i in input[1].split(',') if i != 'x']

    times = [x - (start_time % x) for x in ids]
    min_time = min(times)

    answer1 = ids[times.index(min_time)] * min_time

    print(f'Part 1: {answer1}')

    data = input[1].split(',')

    t = int(data[0])
    step = t
    for index, bus_id in enumerate(data[1:], start=1):
        if bus_id != 'x':
            while (t + index) % int(bus_id) != 0:
                t += step
            step *= int(bus_id)

    print(f'Part 2: {t}')
