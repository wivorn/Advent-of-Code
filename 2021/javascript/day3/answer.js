const fs = require('fs')

const input = fs.readFileSync('input', { encoding: 'utf8', flag: 'r' }).trim().split('\n')


// Part 1
function getGammaEpsilon(input) {
    const total = input.length
    const digits = input[0].length

    let gamma = ''
    let epsilon = ''

    const count = Array(digits).fill(0)

    input.forEach(val => {
        val.split('').forEach((digit, index) => {
            if (digit === '1') {
                count[index]++
            }
        })
    })

    count.map(val => {
        const mostCommon = Math.round(val / total)
        gamma += mostCommon
        epsilon += 1 - mostCommon
    })

    return [gamma, epsilon]
}

const powerConsumption = getGammaEpsilon(input).map((val) => parseInt(val, 2)).reduce((total, value) => total * value, 1)

console.log('Part 1 Answer')
console.log(powerConsumption)

// Part 2
function getMostCommon(arr) {
    return arr.reduce((accum, current) => accum + current, 0) / arr.length >= 0.5 ? 1 : 0
}

function getLeastCommon(arr) {
    return arr.reduce((accum, current) => accum + current, 0) / arr.length < 0.5 ? 1 : 0
}

function getColumn(arr, index) {
    const col = []
    arr.forEach((row) => col.push(row[index]))
    return col
}

function mostCommonFilter(arr, index) {
    const mostCommon = getMostCommon(getColumn(arr, index))
    const filteredList = arr.filter(row => row[index] === mostCommon)
    if (filteredList.length === 1) {
        return filteredList[0]
    }
    
    return mostCommonFilter(filteredList, index + 1)
}

function leastCommonFilter(arr, index) {
    const mostCommon = getLeastCommon(getColumn(arr, index))
    const filteredList = arr.filter(row => row[index] === mostCommon)
    if (filteredList.length === 1) {
        return filteredList[0]
    }
    
    return leastCommonFilter(filteredList, index + 1)
}

function getOxygenGeneratorRating(arr) {
    return parseInt(mostCommonFilter(arr, 0).join(''), 2)
}

function getCO2ScrubberRating(arr) {
    return parseInt(leastCommonFilter(arr, 0).join(''), 2)
}

function getLifeSupportRating(input) {
    const arr = input.map(row => row.split('').map(val => parseInt(val)))
    
    return getOxygenGeneratorRating(arr) * getCO2ScrubberRating(arr)
}

console.log('Part 2 Answer')
console.log(getLifeSupportRating(input))
