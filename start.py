import sys
import os

year = sys.argv[1]
day = sys.argv[2]
lang = sys.argv[3]

try:
    os.mkdir(f'{year}')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/{lang}')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/input')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/{lang}/day{day}')
except OSError:
    print('Folder already exists')
else:
    print('Successfully created the directory')

# Download input
input_path = f'{year}/input/day{day}/input'

try:
    os.system(
        f'curl --silent --show-error --cookie "session=$AOC_SESSION" --output "{input_path}" "https://adventofcode.com/{year}/day/{day}/input"')
except:
    print('No input file')
