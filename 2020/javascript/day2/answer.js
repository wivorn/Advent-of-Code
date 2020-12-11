const fs = require("fs")

const input = fs
    .readFileSync("input", { encoding: "utf8", flag: "r" })
    .split("\n")

function parse(line) {
    const regex = /(\d+)-(\d+) (\w): (\w+)/

    // return [min/pos, max/pos, char, password]
    return regex.exec(line).slice(1)
}

function validate_part1([min, max, char, password]) {
    const charCount = [...password].filter((letter) => letter == char).length

    return charCount >= min && charCount <= max
}

function validate_part2([pos1, pos2, char, password]) {
    return (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char)
}

function validPasswordCount(input, validate) {
    return input
        .map(parse)
        .map(validate)
        .filter((x) => x).length
}

console.log(`Part 1: ${validPasswordCount(input, validate_part1)}`)
console.log(`Part 2: ${validPasswordCount(input, validate_part2)}`)
