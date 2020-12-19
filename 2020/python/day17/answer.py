import os.path
from itertools import product

input_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), '../../input/day17')


class ConwayEngine:
    def __init__(self, input, dimensions):
        self.dimensions = dimensions
        self.active_state = {}
        self.bounds = []

        self.parse(input)
        self.compute_bounds()

    def parse(self, input):
        input = input.strip().split('\n')

        for y in range(len(input)):
            for x, char in enumerate(input[y]):
                if char == '#':
                    position = (x, y, *[0 for _ in range(self.dimensions - 2)])
                    self.active_state[position] = True

    def run(self, count):
        for _ in range(count):
            self.compute_next_state()

    def compute_next_state(self):
        next_active_state = {}

        for position in product(*[[i for i in range(bound[0] - 1, bound[1] + 2)] for bound in self.bounds]):
            active_neighbors_count = self.get_active_neighbours_count(position)
            if (position not in self.active_state and active_neighbors_count == 3) or (position in self.active_state and active_neighbors_count in [2, 3]):
                next_active_state[position] = True

        self.active_state = next_active_state
        self.compute_bounds()

    def compute_bounds(self):
        self.bounds = []
        for i in range(self.dimensions):
            values = [position[i] for position in self.active_state]
            self.bounds.append((min(values), max(values)))

    def get_active_neighbours_count(self, position):
        neighbour_positions = list(product(
            *[[i for i in range(position[dim] - 1, position[dim] + 2)] for dim in range(self.dimensions)]))
        active_positions = [
            current_position for current_position in neighbour_positions if current_position != position and current_position in self.active_state]

        return len(active_positions)

    def print_layer(self, extra_dimension_position):
        (min_x, max_x) = self.bounds[0]
        (min_y, max_y) = self.bounds[1]

        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                if (x, y, *extra_dimension_position) in self.active_state:
                    line += '#'
                else:
                    line += '.'
            print(line)

    def print(self):
        symbols = ['z', 'w']

        for position in product(*[[i for i in range(bound[0], bound[1] + 1)] for bound in self.bounds[2:]]):
            print(', '.join([f'{symbols[index]}: {value}' for index,
                             value in enumerate(position)]))
            self.print_layer(position)
            print('\n')


with open('test_input') as f:
    input = f.read()

    cube = ConwayEngine(input, 3)
    cube.run(6)

    hyper_cube = ConwayEngine(input, 4)
    hyper_cube.run(6)

    print(f'Part 1: {len(cube.active_state)}')
    print(f'Part 2: {len(hyper_cube.active_state)}')
