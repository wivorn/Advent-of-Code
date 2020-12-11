import re

def parse(line):
  parsed = re.search('(\d+)-(\d+) (\w): (\w+)', line)
  return (int(parsed.group(1)), int(parsed.group(2)), parsed.group(3), parsed.group(4))

def validate_part1(min, max, char, password):
  return min <= password.count(char) <= max

def validate_part2(pos1, pos2, char, password):
  return (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char)

def valid_password_count(input, validate):
  return len([True for x in input if validate(*x) ])

with open('input') as f:
  input = [ parse(x) for x in f.read().split('\n')]
  
  print(f'Part 1: {valid_password_count(input, validate_part1)}')
  print(f'Part 2: {valid_password_count(input, validate_part2)}')
  
