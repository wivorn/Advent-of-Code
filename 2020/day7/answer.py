import re


def parse(line):
    line = re.sub(' bags?', '', line).replace('.', '')
    [color, content] = line.split(' contain ')
    contain = {}

    content = content.split(', ')
    for i in content:
        if i == 'no other':
            break

        match = re.search('(\d+) ([\w\s]+)', i)
        contain[match.group(2)] = int(match.group(1))

    return color, contain


def findBagsWith(data, target_colors):
    if len(target_colors) == 0:
        return 0

    processing = [color for color, content in data.items() if any(
        x in target_colors for x in content.keys())]

    filter_data = {key: value for key,
                   value in data.items() if not key in processing}

    return len(processing) + findBagsWith(filter_data, processing)


def findTotalBagsWith(data, target_color):
    if not data[target_color]:
        return 0

    total = 0

    for key, value in data[target_color].items():
        total += value + value * findTotalBagsWith(data, key)

    return total


with open('input') as f:
    data = {}

    for line in f.read().strip().split('\n'):
        color, contain = parse(line)
        data[color] = contain

    print(f'Part 1: {findBagsWith(data, ["shiny gold"])}')
    print(f'Part 2: {findTotalBagsWith(data, "shiny gold")}')
