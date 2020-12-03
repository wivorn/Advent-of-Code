const fs = require('fs')

const input = fs.readFileSync('input', { encoding: 'utf8', flag: 'r' }).split('\n').map(x => parseInt(x))

function getProductPair(input, sum) {
  const found = new Set()
  for (const i of input) {
    let pair = sum - i
    
    if (found.has(pair)) {
      return i * pair
    }
    found.add(i)
  }
}

function getProductTriplet(input, sum) {
  for (let i = 0; i < input.length - 2; i++) {
    const pairSum = sum - input[i]
    const found = new Set()
    for (let j = i + 1; j < input.length; j++) {
      let pair = pairSum - input[j]

      if (found.has(pair)) {
        return input[i] * input[j] * pair
      }
      found.add(input[j])
    }
  }
}

console.log(`Part 1: ${getProductPair(input, 2020)}`)
console.log(`Part 2: ${getProductTriplet(input, 2020)}`)