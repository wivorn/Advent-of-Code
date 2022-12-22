const fs = require("fs")

const input = fs.readFileSync("../../input/day8/input", { encoding: "utf8", flag: "r" })
const example = fs.readFileSync("../../input/day8/example", { encoding: "utf8", flag: "r" })

const map = input.split('\n').filter(c => c).map(row => row.split('').map(i => parseInt(i)))

function visible(map) {
    const columns = map[0].length
    const rows = map.length
    let count = 0
    const scores = []

    function checkTop(row, col) {
        let count = 0
        for (let i = row - 1; i >= 0; i--) {
            if (map[i][col] >= map[row][col]) {
                return [false, count + 1]
            } else {
                count++
            }
        }
        return [true, count]
    }

    function checkBottom(row, col) {
        let count = 0
        for (let i = row + 1; i < rows; i++) {
            if (map[i][col] >= map[row][col]) {
                return [false, count + 1]
            } else {
                count++
            }
        }
        return [true, count]
    }

    function checkLeft(row, col) {
        let count = 0
        for (let i = col - 1; i >= 0; i--) {
            if (map[row][i] >= map[row][col]) {
                return [false, count + 1]
            } else {
                count++
            }
        }
        return [true, count]
    }

    function checkRight(row, col) {
        let count = 0
        for (let i = col + 1; i < columns; i++) {
            if (map[row][i] >= map[row][col]) {
                return [false, count + 1]
            } else {
                count++
            }
        }
        return [true, count]
    }

    for (let j = 0; j < rows; j++) {
        for (let i = 0; i < columns; i++) {
            const [top, topCount] = checkTop(j,i)
            const [bottom, bottomCount] = checkBottom(j,i)
            const [left, leftCount] = checkLeft(j,i)
            const [right, rightCount] = checkRight(j,i)
            if (top || bottom || left || right) {
                count++
            }
            scores.push(topCount * bottomCount * leftCount * rightCount)
        }
    }


    return [count, Math.max(...scores)]
}

const [answer1, answer2] = visible(map)
console.log(answer1)
console.log(answer2)
