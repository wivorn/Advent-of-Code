import re


def parse(input):
    return input.replace('\n\n', ',').replace('\n', ' ').split(',')


def countUnique(group):
    return len(set(''.join(group)))


def countSame(group):
    return len(set.intersection(*[set(i) for i in group]))


with open('input') as f:
    input = parse(f.read())
    choices = [i.strip().split(' ') for i in input]

    print(f'Part 1: {sum([countUnique(i) for i in choices])}')
    print(f'Part 2: {sum([countSame(i) for i in choices])}')
