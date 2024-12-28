# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

ti = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".split("\n")[1:-1]


nexts = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def sol0(inp):
    r = 0
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            for nexter in nexts:
                x, y = j, i
                for c in "XMAS":
                    if y < 0 or x < 0 or y >= len(inp) or x >= len(inp[y]) or c != inp[y][x]:
                        break
                    x += nexter[0]
                    y += nexter[1]
                else:
                    r += 1
    return r


def sol1(inp):
    r = 0
    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[i]) - 1):
            s = [inp[i-1][j-1], inp[i-1][j+1], inp[i+1][j-1], inp[i+1][j+1]]
            if (
                inp[i][j] == "A"
                and sum(1 for c in s if c == "M") == 2
                and sum(1 for c in s if c == "S") == 2
                and inp[i-1][j-1] != inp[i+1][j+1]
            ):
                r += 1
    return r


assert sol0(ti) == 18
assert sol1(ti) == 9


with open("input.txt") as f:
    in_s = f.read().split("\n")[:-1]

print(sol0(in_s))
print(sol1(in_s))
