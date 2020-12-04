const fs = require("fs")

const input = fs
    .readFileSync("input", { encoding: "utf8", flag: "r" })

function parse(input) {
  return input.split('\n\n').map(line => {
    return line
      .replace(/\n/g, ' ').split(' ')
      .reduce((prev, curr) => {
        [key, value] = curr.split(':')
        prev[key] = value
        return prev
      }, {})
  })
}

const REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

// Just for fun
const VALIDATION_RULES = {
  byr: /^19[2-9][0-9]|200[0-2]$/,
  iyr: /^201[0-9]|2020$/,
  eyr: /^202[0-9]|2030$/,
  hgt: /^(1[5-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$/,
  hcl: /^#[0-9a-f]{6}$/,
  ecl: /^amb|blu|brn|gry|grn|hzl|oth$/,
  pid: /^[0-9]{9}$/
}

const hasRequiredFields = requiredFields => passport => requiredFields.filter(key => passport[key]).length == requiredFields.length

const hasValidFields = (requiredFields, validationRules) => passport => requiredFields.filter(key => validationRules[key].test(passport[key])).length == requiredFields.length

const passports = parse(input)

console.log(`Part 1: ${passports.filter(hasRequiredFields(REQUIRED_FIELDS)).length}`)
console.log(`Part 2: ${passports.filter(hasValidFields(REQUIRED_FIELDS, VALIDATION_RULES)).length}`)
