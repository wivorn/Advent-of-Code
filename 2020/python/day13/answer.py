import os.path

input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../input/day13')

with open(input_path) as f:
    input = f.read().strip().split('\n')

    start_time = int(input[0])
    ids = [int(i) for i in input[1].split(',') if i != 'x']

    # times = [x - (start_time % x) for x in ids]
    # min_time = min(times)

    # answer1 = ids[times.index(min_time)] * min_time

    # print(f'Part 1: {answer1}')

    data = input[1].split(',')
    
    # print(ids)
    # [41, 37, 379, 23, 13, 17, 29, 557, 19]
    # number_positions = [data.index(str(x)) for x in ids]
    # print(number_positions)
    # [0, 35, 41, 49, 54, 58, 70, 72, 91]
    # print([data[int(data[x]) + x] for x in number_positions if int(test_data[x]) + x < len(test_data)])
    # ['379', '557', '557', 'x', 'x']
    # [41+0, 37+35, 23+49]

    # equations
    # t = 41a
    # t+35 = 37b
    # t+41 = 379c
    # t+49 = 23d
    # t+54 = 13e
    # t+58 = 17f
    # t+70 = 29g
    # t+72 = 557h
    # t+91 = 19i
    
    # relations
    # t+41 = 41a + 41 = 379c
    # t+72 = 37b + 37 = 557h
    # t+72 = 23d + 23 = 557h

    # a = (379/41)c - 1
    # b = (557/37)h - 1
    # d = (557/23)h - 1

    # solve
    # t = 41a
    # t+35 = 37b
    # t+41 = 379c
    # t+49 = 23d
    # t+54 = 13e
    # t+58 = 17f
    # t+70 = 29g
    # t+72 = 557h
    # t+91 = 19i

    factor_pairs = [(72, 557), (41, 379), (0, 41), (35, 37), (70,29), (49, 23), (91, 19), (58, 17), (54, 13)]

    h = 0
    t = 0
    success = False
    while not success:
        success = True
        h += 851
        t = 557 * h - 72
        print(t)
        for i in factor_pairs:
            if (t + i[0]) % i[1] != 0:
                success = False
                break
    
    print(f'Part 2: {t}')
