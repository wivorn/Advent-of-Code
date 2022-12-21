const fs = require("fs")

const input = fs.readFileSync("../../input/day6/input", { encoding: "utf8", flag: "r" })

const example = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

function findMarker(line, size) {
    const window = []
    for (const [i, c] of line.split('').entries()) {
        if (window.length < size) {
            window.push(c)
        } else {
            const set = new Set(window)
            if (set.size === size) {
                return i
            }
            window.push(c)
            window.shift()
        }
    }
}

// answer1
console.log(findMarker(input, 4))
// answer2
console.log(findMarker(input, 14))
