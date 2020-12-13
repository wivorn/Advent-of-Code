import os.path
import math

input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../input/day12')

def part1(input):
    x, y = 0,0 # initial coordinate
    direction = 0

    for i in input:
        if i[0] == 'N':
            y += i[1]
        elif i[0] == 'S':
            y -= i[1]
        elif i[0] == 'E':
            x += i[1]
        elif i[0] == 'W':
            x -= i[1]
        elif i[0] == 'L':
            direction += i[1]
        elif i[0] == 'R':
            direction -= i[1]
        elif i[0] == 'F':
            x += round(math.cos(math.radians(direction))) * i[1]
            y += round(math.sin(math.radians(direction))) * i[1]

    return abs(x) + abs(y)

def rotate(angle, x, y):
    rx = round(x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle)))
    ry = round(x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle)))
    
    return rx, ry

def part2(input):
    x, y = 0, 0
    wp_x, wp_y = 10, 1

    for i in input:
        if i[0] == 'N':
            wp_y += i[1]
        elif i[0] == 'S':
            wp_y -= i[1]
        elif i[0] == 'E':
            wp_x += i[1]
        elif i[0] == 'W':
            wp_x -= i[1]
        elif i[0] == 'L':
            wp_x, wp_y = rotate(i[1], wp_x, wp_y)
        elif i[0] == 'R':
            wp_x, wp_y = rotate(-i[1], wp_x, wp_y)
        elif i[0] == 'F':
            x += wp_x * i[1]
            y += wp_y * i[1]

    return abs(x) + abs(y)

with open(input_path) as f:
    input = [[x[0], int(x[1:])] for x in f.read().strip().split('\n')]

    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')
