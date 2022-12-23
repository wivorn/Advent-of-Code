const fs = require("fs")

const input = fs.readFileSync("../../input/day9/input", { encoding: "utf8", flag: "r" })
const example = fs.readFileSync("../../input/day9/example", { encoding: "utf8", flag: "r" })
const example2 = fs.readFileSync("../../input/day9/example2", { encoding: "utf8", flag: "r" })

const instructions = input.split('\n').filter(c => c).map(i => i.split(' '))

function isAdjacent(pos1, pos2) {
    return Math.abs(pos1[0] - pos2[0]) <= 1 && Math.abs(pos1[1] - pos2[1]) <= 1 ? true : false
}

function moveHead(head, direction) {
    if (direction === 'U') {
        head[1]++
    } else if (direction === 'D') {
        head[1]--
    } else if (direction === 'L') {
        head[0]--
    } else if (direction === 'R') {
        head[0]++
    }
}

function moveTail(head, tail, direction) {
    if (!isAdjacent(head, tail)) {
        if (tail[0] < head[0]) {
            tail[0]++
        } else if (tail[0] > head[0]) {
            tail[0]--
        }

        if (tail[1] < head[1]) {
            tail[1]++
        } else if (tail[1] > head[1]) {
            tail[1]--
        }
    }
}

function simulate(instructions, size) {
    const rope = Array.from({length: size}, e => Array(2).fill(0))
    let tailVisited = new Set()

    instructions.forEach(instruction => {
        const [direction, step] = instruction
        for (let i = 0; i < step; i++) {
            moveHead(rope[0], direction)
            for (let j = 0; j < size - 1; j++) {
                moveTail(rope[j], rope[j+1], direction)
            }
            tailVisited.add(rope[size - 1].join(','))
        }
    })

    return tailVisited.size
}

function print(rope) {
    const width = 26
    const height = 21
    const originX = 11
    const originY = 5

    const map = Array.from({length: height}, e => Array(width).fill('.'))
    rope.forEach((pos, index) => {
        if (map[height - 1 - pos[1] - originY][pos[0] + originX] === '.')
            map[height - 1 - pos[1] - originY][pos[0] + originX] = index === 0 ? 'H' : index
    })
    map.forEach(row => { console.log(row.join(''), '\n') })
    console.log('\n\n')
}

// const answer1 = simulate(instructions, 2)
const answer2 = simulate(instructions, 10)

// console.log(answer1)
console.log(answer2)
