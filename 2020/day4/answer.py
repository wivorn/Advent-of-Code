import re

def parse(input):
  return [{ x.split(':')[0]: x.split(':')[1] for x in p } for p in [[x for x in re.split('\n|\s', p)] for p in input.split('\n\n')]]

def validate_year(year, digits, start, end):
  if len(year) != digits:
    return False
  
  return start <= int(year) <= end

def validate_height(height):
  match = re.search('(\d+)(in|cm)', height)
  if not match:
    return False

  value, unit = match.group(1), match.group(2)

  if unit == 'cm':
    return 150 <= int(value) <= 193
  if unit == 'in':
    return 59 <= int(value) <= 76

def validate_hair_color(hair_color):
  return re.match('^#[0-9a-f]{6}$', hair_color)

def validate_eye_color(eye_color):
  return eye_color in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }

def validate_pid(pid):
  return re.match('^[0-9]{9}$', pid)

def validate_part1(passport):
  field_rules = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

  return field_rules.issubset(set(passport.keys()))

def validate_part2(passport):
  return (validate_part1(passport) and
          validate_year(passport['byr'], 4, 1920, 2002) and
          validate_year(passport['iyr'], 4, 2010, 2020) and
          validate_year(passport['eyr'], 4, 2020, 2030) and
          validate_height(passport['hgt']) and
          validate_hair_color(passport['hcl']) and
          validate_eye_color(passport['ecl']) and
          validate_pid(passport['pid']))
  
def valid_count(passports, validate):
  return len([ True for p in passports if validate(p) ])

with open('input') as f:
  input = f.read()
  passports = parse(input)

  print(f'Part 1: {valid_count(passports, validate_part1)}')
  print(f'Part 2: {valid_count(passports, validate_part2)}')