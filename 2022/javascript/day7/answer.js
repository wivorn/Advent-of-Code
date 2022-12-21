const fs = require("fs")

const input = fs.readFileSync("../../input/day7/input", { encoding: "utf8", flag: "r" })
const example = fs.readFileSync("../../input/day7/example", { encoding: "utf8", flag: "r" })

const commands = input.split('\n').filter(c => c)

class File {
    constructor(name, size, parent) {
        this.name = name
        this.size = size
        this.parent = parent
    }
}

class Directory {
    constructor(name, parent = null) {
        this.name = name
        this.children = {}
        this.parent = parent
        this.size = 0
    }
}

class System {
    constructor(rootDirectory) {
        this.root = new Directory(rootDirectory)
    }

    createDirectory(currentDirectory, name) {
        currentDirectory.children[name] = new Directory(name, currentDirectory)
        return currentDirectory.children[name]
    }

    createFile(currentDirectory, name, size) {
        size = parseInt(size)
        currentDirectory.children[name] = new File(name, size, currentDirectory)
        currentDirectory.size += size
        while (currentDirectory.parent !== null) {
            currentDirectory = currentDirectory.parent
            currentDirectory.size += size
        }
    }
}

class Terminal {
    constructor() {
        this.system = new System('/')
        this.currentDirectory = null
    }

    run(command) {
        if (command.includes('$ cd')) {
            const [, param] = command.match(/\$ cd (.*)/)
            switch (param) {
                case '/':
                    this.currentDirectory = this.system.root
                    break
                case '..':
                    this.currentDirectory = this.currentDirectory.parent
                    break
                default:
                    this.currentDirectory = this.currentDirectory.children[param]
                    break
            }
        } else if (command.includes('$ ls')) {
            // do nothing
        } else if (command.includes('dir')) {
            // write directory
            const [, name] = command.match(/dir (.*)/)
            this.system.createDirectory(this.currentDirectory, name)
        } else if (command.match(/([0-9]+) (.*)/)[0]) {
            // write file
            const [, size, name] = command.match(/([0-9]+) (.*)/)
            this.system.createFile(this.currentDirectory, name, size)
        }
    }

    getDirectories() {
        const queue = [this.system.root]
        const directories = []
        while (queue.length) {
            const current = queue.pop()
            directories.push(current)
            Object.values(current.children).forEach((entity) => {
                if (entity.children) {
                    queue.push(entity)
                }
            })
        }
        return directories
    }
}

const terminal = new Terminal()

commands.forEach(command => {
    terminal.run(command)
})

const answer1 = terminal.getDirectories().filter(dir => dir.size <= 100000).reduce((sum, dir) => (sum + dir.size), 0)
// console.log(answer1)

const totalDiskSize = 70000000
const current = terminal.system.root.size
const spaceLeft = totalDiskSize - current
const deleteSize = 30000000 - spaceLeft

const answer2 = Math.min(...terminal.getDirectories().filter(dir => dir.size > deleteSize).map(dir => dir.size))
console.log(answer2)
