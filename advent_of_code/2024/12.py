# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

def sol0(ci):
    ci = [[v for v in l] for l in ci]
    height = len(ci)
    width = len(ci[0])
    cur_zone = 0
    for y, l in enumerate(ci):
        for x, c in enumerate(l):
            if isinstance(c, str):
                clean0(ci, x, y, width, height, c, cur_zone)
                cur_zone += 1
    sols = {}
    for y, l in enumerate(ci):
        for x, c in enumerate(l):
            if c not in sols:
                sols[c] = [0, 0]
            sols[c][0] += 1
            if x == 0 or ci[y][x-1] != c:
                sols[c][1] += 1
            if x == width - 1 or ci[y][x+1] != c:
                sols[c][1] += 1
            if y == 0 or ci[y-1][x] != c:
                sols[c][1] += 1
            if y == height - 1 or ci[y+1][x] != c:
                sols[c][1] += 1
    return sum(a * b for a, b in sols.values())


def clean0(ci, x, y, width, height, c, cur_zone):
    if not 0 <= x < width or not 0 <= y < height:
        return
    if ci[y][x] != c:
        return
    ci[y][x] = cur_zone
    clean0(ci, x+1, y, width, height, c, cur_zone)
    clean0(ci, x-1, y, width, height, c, cur_zone)
    clean0(ci, x, y+1, width, height, c, cur_zone)
    clean0(ci, x, y-1, width, height, c, cur_zone)


def sol1(ci):
    ci = [[v for v in l] for l in ci]
    height = len(ci)
    width = len(ci[0])
    cur_zone = 0
    for y, l in enumerate(ci):
        for x, c in enumerate(l):
            if isinstance(c, str):
                clean0(ci, x, y, width, height, c, cur_zone)
                cur_zone += 1
    sols = {}
    g = lambda x, y: ci[y][x] if 0 <= x < width and 0 <= y < height else None
    for y, l in enumerate(ci):
        prevbar_t = None
        prevbar_b = None
        for x, c in enumerate(l):
            if c not in sols:
                sols[c] = [0, 0]
            sols[c][0] += 1
            if g(x, y - 1) == c:
                prevbar_t = None
            elif prevbar_t != c:
                sols[c][1] += 1
                prevbar_t = c
            # No need for else, prevbar is already c
            if g(x, y + 1) == c:
                prevbar_b = None
            elif prevbar_b != c:
                sols[c][1] += 1
                prevbar_b = c
    for x in range(width):
        prevbar_l = None
        prevbar_r = None
        for y in range(height):
            c = ci[y][x]
            if g(x-1, y) == c:
                prevbar_l = None
            elif prevbar_l != c:
                sols[c][1] += 1
                prevbar_l = c
            # No need for else, prevbar is already c
            if g(x+1, y) == c:
                prevbar_r = None
            elif prevbar_r != c:
                sols[c][1] += 1
                prevbar_r = c
    return sum(a * b for a, b in sols.values())



ti = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""[1:-1].split("\n")

ti2 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""[1:-1].split("\n")

assert(sol0(ti)) == 1930
assert(sol1(ti)) == 1206
assert(sol1(ti2)) == 368



try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
