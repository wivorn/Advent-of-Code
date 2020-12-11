class Node:
  def __init__(self, data):
      self.children = []
      self.data = data

# test = sorted([16,10,15,5,1,11,7,19,6,12,4])
test = [1,2,3]

def getDiffSet(data):
  set = {1: 0, 2: 0, 3: 1}

  set[data[0]] += 1

  for i in range(1, len(data)):
    diff = data[i] - data[i-1]
    set[diff] += 1

  return set

def getTree(data):
  tree = []

  for i in range(0, len(data) - 1):
    j = i + 1
    next = []
    while j < len(data) and (data[j] - data[i]) <= 3:
      next.append(j)
      j += 1
    
    tree.append(next)

  return tree

memo = {}

def countBranches(tree, pos):
  total = 0
  for i in tree[pos]:
    if (i == len(tree)):
      total += 1
    elif i in memo:
      total += memo[i]
    else:
      memo[i] = countBranches(tree, i) 
      total += memo[i]

  return total

with open('input') as f:
  data = sorted([int(x) for x in f.read().strip().split('\n')])
  set1 = getDiffSet(data)

  tree = getTree([0] + data)

  print(f'Part 1: {set1[1] * set1[3]}')
  print(f'Part 2: {countBranches(tree, 0)}')