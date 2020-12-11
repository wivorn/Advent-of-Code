const fs = require("fs");

const parse = (input) =>
    input.split("\n\n").map((group) => group.trim().split("\n"));

const groups = parse(fs.readFileSync("input", { encoding: "utf8", flag: "r" }));

function countUnique(groups) {
    return groups
        .map((group) => {
            set = new Set(group.join(""));
            return set.size;
        })
        .reduce((total, current) => total + current, 0);
}

function countSame(groups) {
    return groups
        .map((group) =>
            group
                .map((line) => new Set(line))
                .reduce(
                    (intersectionSet, set) =>
                        new Set([...intersectionSet].filter((x) => set.has(x))),
                    new Set(group[0])
                )
        )
        .map((set) => set.size)
        .reduce((a, b) => a + b, 0);
}

console.log(`Part 1: ${countUnique(groups)}`);
console.log(`Part 2: ${countSame(groups)}`);
