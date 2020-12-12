import os.path

input_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), '../../input/day2')


class IntCodeVirtualMachine:
    ADD = 1
    MUL = 2
    END = 99

    def __init__(self, raw_code):
        self.code = self.parse(raw_code)
        self.memory = self.code.copy()

    def parse(self, code):
        return [int(x) for x in code.strip().split(',')]

    def reset(self):
        self.memory = self.code.copy()

    def replace(self, position, value):
        self.memory[position] = value

    def read(self, pos):
        return self.memory[pos]

    def run(self):
        ptr = 0
        while ptr < len(self.memory):
            instruction = self.memory[ptr]
            pos1 = self.memory[ptr + 1]
            pos2 = self.memory[ptr + 2]
            pos3 = self.memory[ptr + 3]

            if instruction == self.ADD:
                self.memory[pos3] = self.memory[pos1] + self.memory[pos2]
                ptr += 4
            elif instruction == self.MUL:
                self.memory[pos3] = self.memory[pos1] * self.memory[pos2]
                ptr += 4
            elif instruction == self.END:
                break


def part2(input):
    vm = IntCodeVirtualMachine(input)
    
    for noun in range(0, 100):
        for verb in range(0, 100):
            vm.reset()
            vm.replace(1, noun)
            vm.replace(2, verb)
            vm.run()
            if vm.memory[0] == 19690720:
                return 100 * noun + verb

with open(input_path) as f:
    input = f.read()

    vm = IntCodeVirtualMachine(input)
    vm.replace(1, 12)
    vm.replace(2, 2)
    vm.run()
    
    print(f'Part 1: {vm.read(0)}')
    print(f'Part 2: {part2(input)}')
