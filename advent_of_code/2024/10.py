# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

def sol0(ci):
    ci = [[int(c) for c in l] for l in ci]
    height = len(ci)
    width = len(ci[0])
    return sum(len(paths(ci, 0, width, height, x, y, set())) for y in range(height) for x in range(width))


def sol1(ci):
    ci = [[int(c) for c in l] for l in ci]
    height = len(ci)
    width = len(ci[0])
    return sum(len(paths(ci, 0, width, height, x, y, list())) for y in range(height) for x in range(width))


def paths(ci, i, width, height, x, y, cur_set):
    if not (0 <= x < width and 0 <= y < height):
        pass
    elif ci[y][x] == 9 and i == 9:
        (cur_set.add if isinstance(cur_set, set) else cur_set.append)((x, y))
    elif ci[y][x] == i:
        for nx, ny in ((x-1, y), (x, y-1), (x, y+1), (x+1, y)):
            paths(ci, i+1, width, height, nx, ny, cur_set)
    return cur_set




ti = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""[1:-1].split("\n")


assert(sol0(ti)) == 36
assert(sol1(ti)) == 81


with open("input.txt") as f:
    ri = f.read().split("\n")[:-1]


print(sol0(ri))
print(sol1(ri))
