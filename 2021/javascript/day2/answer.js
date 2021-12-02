const fs = require('fs')

const input = fs.readFileSync('input', { encoding: 'utf8', flag: 'r' }).trim().split('\n').map(x => x.split(' '))

// Part 1
function findPosition(input) {
    let distance = 0
    let depth = 0

    input.forEach(val => {
        const amount = parseInt(val[1])
        switch (val[0]) {
            case 'forward':
                distance += amount
                break
            case 'down':
                depth += amount
                break
            case 'up':
                depth -= amount
                break
            default:
                break
        }
    })

    return distance * depth
}

console.log(findPosition(input))

// Part 2
function findPosition2(input) {
    let distance = 0
    let depth = 0
    let aim = 0

    input.forEach(val => {
        const amount = parseInt(val[1])
        switch (val[0]) {
            case 'forward':
                distance += amount
                depth += aim * amount
                break
            case 'down':
                aim += amount
                break
            case 'up':
                aim -= amount
                break
            default:
                break
        }
    })

    return distance * depth
}

console.log(findPosition2(input))
