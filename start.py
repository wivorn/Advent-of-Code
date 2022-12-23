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
    os.mkdir(f'{year}/input/day{day}')
except OSError:
    print('Folder already exists')

try:
    os.mkdir(f'{year}/{lang}/day{day}')
except OSError:
    print('Folder already exists')
else:
    print('Successfully created the directory')

try:
    if (lang == 'python'):
        f = open(f'{year}/{lang}/day{day}/answer.py', 'w')
        f.writelines([
            'import os.path\n\n',
            f"input_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../input/day{day}')\n\n",
            'with open(input_path) as f:\n',
            '   input = f.read()\n'
        ])
        f.close()
    elif (lang == 'elixir'):
        f = open(f'{year}/{lang}/day{day}/answer.exs', 'w')
        f.writelines([
            f"file = Path.expand('{year}/input/day{day}/input') |> Path.absname()\n",
            'input = File.read!(file)\n\n',
            'IO.inspect(input)'
        ])
        f.close()
    elif (lang == 'javascript'):
        f = open(f'{year}/{lang}/day{day}/answer.js', 'w')
        f.writelines([
            'const fs = require("fs")\n\n',
            f"const input = fs.readFileSync('../../input/day{day}/input', { encoding: 'utf8', flag: 'r' })\n",
            f"const example = fs.readFileSync('../../input/day{day}/example', { encoding: 'utf8', flag: 'r' })\n\n"
        ])
        f.close()
except:
    print('File already exist')

# Download input
input_path = f'{year}/input/day{day}/input'

try:
    os.system(
        f'curl --silent --show-error --cookie "session=$AOC_SESSION" --output "{input_path}" "https://adventofcode.com/{year}/day/{day}/input"')
    f = f = open(f'{year}/input/day{day}/example', "a")
    f.close()
except:
    print('No input file')
