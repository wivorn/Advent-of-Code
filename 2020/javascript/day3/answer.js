const fs = require('fs')

const input = fs
    .readFileSync('input', { encoding: 'utf8', flag: 'r' })
    .split('\n')

const countTrees = (map, right, down) =>
    map
        .filter((_, index) => index && index % down == 0)
        .reduce(
            (count, row, index) =>
                row[((index + 1) * right) % row.length] == '#'
                    ? count + 1
                    : count,
            0
        )

console.log(`Part 1: ${countTrees(input, 3, 1)}`)
console.log(
    `Part 2: ${
        countTrees(input, 1, 1) *
        countTrees(input, 3, 1) *
        countTrees(input, 5, 1) *
        countTrees(input, 7, 1) *
        countTrees(input, 1, 2)
    }`
)
