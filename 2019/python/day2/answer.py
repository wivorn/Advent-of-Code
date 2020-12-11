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
        index = 0
        while index < len(self.memory):
            cmd = self.memory[index]
            pos1 = self.memory[index + 1]
            pos2 = self.memory[index + 2]
            pos3 = self.memory[index + 3]

            if cmd == self.ADD:
                self.memory[pos3] = self.memory[pos1] + self.memory[pos2]
                index += 4
            elif cmd == self.MUL:
                self.memory[pos3] = self.memory[pos1] * self.memory[pos2]
                index += 4
            elif cmd == self.END:
                break

    def debug(self):
        index = 0
        while index < len(self.memory):
            cmd = self.memory[index]
            pos1 = self.memory[index + 1]
            pos2 = self.memory[index + 2]
            pos3 = self.memory[index + 3]

            print('index: ', index)
            print('cmd: ', cmd)
            
            if cmd == self.ADD:
                self.memory[pos3] = self.memory[pos1] + self.memory[pos2]
                index += 4
            elif cmd == self.MUL:
                self.memory[pos3] = self.memory[pos1] * self.memory[pos2]
                index += 4
            elif cmd == self.END:
                break
                
            yield


with open(input_path) as f:
    input = f.read()

    vm = IntCodeVirtualMachine(input)
    vm.replace(1, 12)
    vm.replace(2, 2)
    vm.run()
    
    print(f'Part 1: {vm.read(0)}')
    # print(f'Part 2: ')
