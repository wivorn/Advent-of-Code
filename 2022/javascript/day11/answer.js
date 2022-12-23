const fs = require("fs")

const input = fs.readFileSync("../../input/day11/input", { encoding: "utf8", flag: "r" })
const example = fs.readFileSync("../../input/day11/example", { encoding: "utf8", flag: "r" })

const puzzle = input.split('\n\n').filter(c => c)

class Monkey {
    constructor(items, operation, testParams) {
        this.items = items
        this.operation = (old) => {
            let [_, operator, right] = operation.split(' ')
            right = right === 'old' ? parseInt(old) : parseInt(right)

            if (operator === '+') {
                return old + right
            } else if (operator === '*') {
                return old * right
            }
        }
        this.test = (val) => {
            const [divisor, trueMonkey, falseMonkey] = testParams
            return val % divisor === 0 ? trueMonkey : falseMonkey
        }
        this.inspectCount = 0
    }
}

class MonkeyGame {
    constructor(monkeys) {
        this.monkeys = monkeys
        this.round = 0
    }

    startRound() {
        monkeys.forEach(monkey => {
            while (monkey.items.length) {
                let item = monkey.items.shift()
                item = monkey.operation(item)
                item = Math.floor(item / 3)
                const nextMonkey = monkey.test(item)
                monkey.inspectCount++
                this.monkeys[nextMonkey].items.push(item)
            }
        })
        this.round++
    }

    run(rounds) {
        for (let i = 0; i < rounds; i++) {
            this.startRound()
        }
    }
}

const monkeys = puzzle.map(m => {
    let [, startingItems] = m.match(/items: (.*)/)
    startingItems = startingItems.split(',').map((i) => parseInt(i.trim()))
    let [, operation] = m.match(/new = (.*)/)
    let [, divisor] = m.match(/divisible by (.*)/)
    divisor = parseInt(divisor)
    let [, trueValue] = m.match(/true: throw to monkey (.*)/)
    trueValue = parseInt(trueValue)
    let [, falseValue] = m.match(/false: throw to monkey (.*)/)
    falseValue = parseInt(falseValue)
    return new Monkey(startingItems, operation, [divisor, trueValue, falseValue])
})

const game = new MonkeyGame(monkeys)
game.run(20)
const answer1 = game.monkeys.sort((a, b) => b.inspectCount - a.inspectCount).map(m => m.inspectCount).slice(0, 2).reduce((acc, curr) => acc * curr, 1)
console.log(answer1)
