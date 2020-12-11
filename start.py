import sys
import os

year = sys.argv[1]
day = sys.argv[2]

try:
    os.mkdir(f'{year}')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/python')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/input')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/python/day{day}')
except OSError:
    print('Folder already exists')
else:
    print('Successfully created the directory')

try:
    f = open(f'{year}/python/day{day}/answer.py', mode='w')
    f.writelines([
        "import os.path\n\n",
        f"input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../input/day{day}')\n\n",
        "with open(input_path) as f:\n",
        "    input = f.read().strip().split('\\n')\n\n",
        "    print(f'Part 1: ')\n",
        "    print(f'Part 2: ')\n"
    ])
    f.close()
except:
    print('File already exist')

# Download input
input_path = f'{year}/input/day{day}'

try:
    os.system(
        f'curl --silent --show-error --cookie "session=$AOC_SESSION" --output "{input_path}" "https://adventofcode.com/{year}/day/{day}/input"')
except:
    print('No input file')
