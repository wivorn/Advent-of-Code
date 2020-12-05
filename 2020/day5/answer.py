import math

def getPosition(line):
  row = [0, 127]
  col = [0, 7]

  for letter in line[0:7]:
    if letter == 'F':
      row[1] = math.floor(sum(row) / 2)
    elif letter == 'B':
      row[0] = math.ceil(sum(row) / 2)

  for letter in line[7:10]:
    if letter == 'L':
      col[1] = math.floor(sum(col) / 2)
    elif letter == 'R':
      col[0] = math.ceil(sum(col) / 2)

  return [row[0], col[0]]

def getID(position):
  return position[0] * 8 + position[1]

def findMissingID(ids):
  current = ids[0]
  for id in ids:
    if current != id:
      break
    current += 1
  return current

with open('input') as f:
  input = f.read().split('\n')
  ids = [getID(getPosition(line)) for line in input ]
  ids.sort()
  
  print(f'Part 1: {ids[-1]}')
  print(f'Part 2: {findMissingID(ids)}')