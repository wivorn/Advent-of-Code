const fs = require("fs")

const input = fs.readFileSync("input", { encoding: "utf8", flag: "r" }).split('\n')

function getPosition(data) {
  const row = data.substring(0, 7).split('').reduce((pos, letter) => letter == 'F' ? [pos[0], Math.floor((pos[0] + pos[1]) / 2)] : [Math.ceil((pos[0] + pos[1]) / 2),pos[1]], [0, 127])[0]
  const col = data.substring(7).split('').reduce((pos, letter) => letter == 'L' ? [pos[0], Math.floor((pos[0] + pos[1]) / 2)] : [Math.ceil((pos[0] + pos[1]) / 2),pos[1]], [0, 7])[0]
  
  return [row, col]
}

const getID = position => position[0] * 8 + position[1]

const sortedIDs = input.map(getPosition).map(getID).sort((a, b) => a - b)
const missingID = sortedIDs.filter((val, index) => sortedIDs[index - 1] && val - sortedIDs[index - 1] > 1 ? true : false ) - 1

console.log(`Part 1: ${sortedIDs[sortedIDs.length - 1]}`)
console.log(`Part 2: ${missingID}`)