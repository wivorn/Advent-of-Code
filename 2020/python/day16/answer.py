import os.path
import math

input_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), '../../input/day16')


def isValidValue(rules, value):
    for ranges in list(rules.values()):
        for [min, max] in ranges:
            if min <= value <= max:
                return True

    return False


def isValidTicket(rules, ticket):
    for value in ticket:
        if not isValidValue(rules, value):
            return False

    return True


def matchRule(rule, values):
    valid_count = 0
    for value in values:
        for [min, max] in rule:
            if min <= value <= max:
                valid_count += 1

    if valid_count == len(values):
        return True

    return False


def resolveOrder(valid_rules):
    # get all single rules
    processed = {}
    while len(valid_rules) > 0:
        processing = {k: list(v)[0]
                      for k, v in valid_rules.items() if len(v) == 1}
        valid_rules = {k: v for k, v in valid_rules.items() if len(v) > 1}

        for value_to_remove in processing.values():
            for k, v in valid_rules.items():
                if value_to_remove in v:
                    valid_rules[k].remove(value_to_remove)

        processed = processed | processing

    return processed


def getFieldOrder(rules, tickets):
    # {0: {'row'}, 1: {'row', 'class'}, 2: {'seat', 'row', 'class'}}
    valid_rules = {}
    for position in range(len(tickets[0])):
        values = [ticket[position] for ticket in tickets]
        for name, rule in rules.items():
            if matchRule(rule, values):
                if not position in valid_rules:
                    valid_rules[position] = {name}
                else:
                    valid_rules[position].add(name)

    # {0: 'row', 1: 'class', 2: 'seat'}
    return resolveOrder(valid_rules)


with open(input_path) as f:
    # Parse
    input = f.read().strip().split('\n\n')

    # example: {'class': [[1, 3], [5, 7]], 'row': [[6, 11], [33, 44]], 'seat': [[13, 40], [45, 50]]}
    rules = {line.split(': ')[0]: [[int(j) for j in i.split('-')] for i in line.split(': ')[1].split(
        ' or ')] for line in input[0].strip().split('\n')}

    # example: [7, 1, 14]
    my_ticket = [int(i) for i in input[1].split('\n')[1].split(',')]

    # example: [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]
    nearby_tickets = [[int(i) for i in ticket.split(',')]
                      for ticket in input[2].split('\n')[1:]]

    # Part 1
    error_values = [value for ticket in nearby_tickets for value in ticket if not isValidValue(
        rules, value)]

    print(f'Part 1: {sum(error_values)}')

    # Part 2
    valid_tickets = [
        ticket for ticket in nearby_tickets if isValidTicket(rules, ticket)]

    field_orders = getFieldOrder(rules, valid_tickets)

    departure_values = [my_ticket[k]
                        for k, v in field_orders.items() if 'departure' in v]

    print(f'Part 2: {math.prod(departure_values)}')
