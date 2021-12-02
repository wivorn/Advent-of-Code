const fs = require('fs')

const input = fs.readFileSync('input', { encoding: 'utf8', flag: 'r' }).split('\n').map(x => parseInt(x))

// Part 1
function totalIncrease(arr) {
    return arr.reduce((total, curr, index, arr) => {
        if (index > 0 && curr > arr[index - 1]) {
            total++
        }
        return total
    }, 0)
}

console.log(totalIncrease(input))

// Part 2
const slidingWindow = input.map((val, index, arr) => {
    if (index + 2 < arr.length) {
        return val + arr[index + 1] + arr[index + 2]
    }
    return 0
})

console.log(totalIncrease(slidingWindow))
