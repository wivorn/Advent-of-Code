const fs = require("fs")

const input = fs.readFileSync("../../input/day10/input", { encoding: "utf8", flag: "r" })
const example = fs.readFileSync("../../input/day10/example", { encoding: "utf8", flag: "r" })

const instructions = input.split('\n').filter(c => c)

const screenWidth = 40
const screenHeight = 6

class Computer {
    constructor() {
        this.instructions = []
        this.clock = 0
        this.register = {
            x: 1
        }
        this.sum = 0
        this.crt = Array.from({ length: screenHeight }, e => Array(screenWidth).fill(''))
    }

    load(instructions) {
        this.instructions = instructions
    }

    tick() {
        this.updateScreen()
        this.clock++
        this.updateSum()
    }

    exec(instruction) {
        const [command, value] = instruction.split(' ')
        switch (command) {
            case 'noop':
                this.tick()
                break
            case 'addx':
                this.tick()
                this.tick()
                this.register.x += parseInt(value)
                break
            default:
                break
        }
    }

    run() {
        this.instructions.forEach(instruction => {
            this.exec(instruction)
        })
    }

    updateSum() {
        if ((this.clock - 20) % 40 == 0 && this.clock <= 220) {
            this.sum += this.clock * this.register.x
        }
    }

    updateScreen() {
        const col = this.clock % 40
        const row = Math.floor(this.clock / 40)
        this.crt[row][col] =  col >= this.register.x - 1 && col <= this.register.x + 1 ? 'X' : ' '
    }

    print() {
        console.log(`signal strength: ${this.sum}`)
    }

    draw() {
        this.crt.forEach(row => {
            console.log(row.join(''))
        })
    }
}

const computer = new Computer()

computer.load(instructions)
computer.run()
// answer1
computer.print()
// answer2
computer.draw()
