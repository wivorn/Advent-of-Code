const fs = require("fs")

const input = fs.readFileSync("../../input/day5/input", { encoding: "utf8", flag: "r" })

const [puzzle, instruction] = input.split('\n\n')

const data = puzzle.split('\n')
data.pop()
const instructions = instruction.split('\n').filter(i => i)

function chunk(input, chunkSize) {
    const arr = []
    for (let i = 0; i < input.length; i += chunkSize) {
        arr.push(input.slice(i, i + chunkSize).trim().replace(/(\[|\])/g, ''))
    }
    return arr
}

const stacks = data.reverse().reduce((acc, row) => {
    chunk(row, 4).forEach((c, idx) => {
        if (c) {
            if (acc[idx]) {
                acc[idx].push(c)
            } else {
                acc[idx] = [c]
            }
        }
    })
    return acc
}, [])

const stacks2 = data.reduce((acc, row) => {
    chunk(row, 4).forEach((c, idx) => {
        if (c) {
            if (acc[idx]) {
                acc[idx].push(c)
            } else {
                acc[idx] = [c]
            }
        }
    })
    return acc
}, [])

function run(stacks, instructions) {
    instructions.forEach(instruction => {
        const [_, count, from, to] = instruction.match(/move ([0-9]+) from ([0-9]+) to ([0-9]+)/)
        stacks[to - 1].push(...stacks[from - 1].splice(stacks[from - 1].length - count).reverse())
    })
}

function run2(stacks, instructions) {
    instructions.forEach(instruction => {
        const [_, count, from, to] = instruction.match(/move ([0-9]+) from ([0-9]+) to ([0-9]+)/)
        stacks[to - 1].push(...stacks[from - 1].splice(stacks[from - 1].length - count))
    })
}

function getLast(arr) {
    return arr.reduce((str, row) => {
        return str += row[row.length - 1]
    }, '')
}

run(stacks, instructions)
const answer1 = getLast(stacks)
console.log(answer1)

run2(stacks2, instructions)
const answer2 = getLast(stacks2)
console.log(answer2)
