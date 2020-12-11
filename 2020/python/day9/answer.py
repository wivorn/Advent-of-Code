from itertools import combinations

def getCombinationSum(data):
    return set([sum(x) for x in list(combinations(data, 2))])

def findInvalid(data, preamble_size):
    for i in range(preamble_size, len(data)):
        sum_set = getCombinationSum([data[x] for x in range(i - preamble_size, i)])
        if data[i] in sum_set:
            continue
        else:
            return data[i]

def findInvalidSet(data, invalid_number):
    for i in range(len(data)):
        arr = []
        for j in range(i, len(data)):
            arr.append(data[j])
            
            if sum(arr) == invalid_number:
                return min(arr) + max(arr)

with open('input') as f:
    data = [int(x) for x in f.read().split('\n')]
    
    invalid_number = findInvalid(data, 25)
    
    print(f'Part 1: {invalid_number}')
    print(f'Part 2: {findInvalidSet(data, invalid_number)}')