def countTrees(map, right, down):
  col = 0
  trees = 0
  width = len(map[0])

  for row in range(down, len(map), down):
    col += right

    if map[row][col % width] == '#':
      trees += 1

  return trees

with open('input') as f:
  input = f.read().split('\n')
  
  print(f'Part 1: {countTrees(input, 3, 1)}')
  print(f'Part 2: {countTrees(input, 1, 1) * countTrees(input, 3, 1) * countTrees(input, 5, 1) * countTrees(input, 7, 1) * countTrees(input, 1, 2)}')