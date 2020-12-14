import os.path
import re
from itertools import product

input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../input/day14')

def apply(mask, value):
    value = f'{value:036b}'
    new_value = ''
    for index, bit in enumerate(value):
        if mask[index] == 'X':
            new_value = new_value + bit
        else:
            new_value = new_value + mask[index]
    
    return int(new_value, 2)

def getAddresses(mask, address_binary):
    addresses = []
    temp_address = ''
    x_count = 0
    for index, bit in enumerate(address_binary):
        if mask[index] == '0':
            temp_address = temp_address + bit
        elif mask[index] == '1':
            temp_address = temp_address + '1'
        else:
            temp_address = temp_address + 'X'
            x_count += 1

    list = ["".join(seq) for seq in product('01', repeat=x_count)]
    for combo in list:
        new_address = temp_address
        for bit in combo:
            new_address = new_address.replace('X', bit, 1)
        
        addresses.append(new_address)

    return [int(a, 2) for a in addresses]

with open(input_path) as f:
    data = f.read().strip().split('\n')
    mask = ''
    mem = {}

    for line in data:
        [left, right] = line.split(' = ')
        
        if (left == 'mask'):
            mask = right
        else:
            mem[left] = apply(mask, int(right))

    print(f'Part 1: {sum(mem.values())}')

    mem = {}
    for line in data:
        [left, right] = line.split(' = ')

        if (left == 'mask'):
            mask = right
        else:
            address = int(re.search('(\d+)', left).group(1))
            address_binary = f'{address:036b}'
            addresses = getAddresses(mask, address_binary)
            for i in addresses:
                mem[i] = int(right)

    print(f'Part 2: {sum(mem.values())}')
