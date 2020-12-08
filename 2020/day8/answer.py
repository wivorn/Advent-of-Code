import copy


def parse(line):
    instruction, value = line.split(' ')
    return [instruction, int(value)]


def run(program):
    visited = set()
    accum = 0
    index = 0

    while not index in visited:
        if index == len(program):
            return True, accum

        visited.add(index)

        (cmd, val) = program[index]

        if cmd == 'nop':
            index += 1
        elif cmd == 'acc':
            visited.add(index)
            accum += val
            index += 1
        elif cmd == 'jmp':
            index += val

    return False, accum


def replace(program, instruction, index):
    new_program = copy.deepcopy(program)

    if instruction == 'nop':
        new_program[index][0] = 'jmp'
    elif instruction == 'jmp':
        new_program[index][0] = 'nop'

    return new_program


with open('input') as f:
    program = [parse(x) for x in f.read().strip().split('\n')]

    # brute force
    # find all nop and jump index
    list = [(x[0], index) for index, x in enumerate(
        program) if x[0] == 'jmp' or x[0] == 'nop']

    all_programs = [run(replace(program, *i)) for i in list]

    answer2 = [x for x in all_programs if x[0] == True]

    print(f'Part 1: {run(program)[1]}')
    print(f'Part 2: {answer2[0][1]}')
