# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf


def sol0(ci, limit):
    return solv(ci, limit, 2)


def sol1(ci, limit):
    return solv(ci, limit, 20)


def solv(ci, limit, passings):
    passings = make_passings(passings)
    width, height, start, end, g = consume(ci)
    ngs = gen_cheesy_djikstra_grid(width, height, g, start)
    no_cheat_end_time = ngs[end[1]][end[0]]
    nge = gen_cheesy_djikstra_grid(width, height, g, end)
    starters = ((sx, sy) for sx in range(width) for sy in range(height) if ngs[sy][sx] < no_cheat_end_time)
    return sum(
        1
        for sx, sy in starters for ex, ey, cu in ((sx + ax, sy + ay, ccu) for (ax, ay), ccu in passings)
        if 0 <= ex < width and 0 <= ey < height and ngs[sy][sx] + nge[ey][ex] + cu <= no_cheat_end_time - limit
    )


def consume(ci):
    width, height = len(ci[0]), len(ci)
    start = [(x, y) for y in range(height) for x in range(width) if ci[y][x] == "S"][0]
    end = [(x, y) for y in range(height) for x in range(width) if ci[y][x] == "E"][0]
    tg = [[c != "#" for c in l] for l in ci]
    g = lambda x, y: 0 <= x < width and 0 <= y < height and tg[y][x]
    return width, height, start, end, g


def gen_cheesy_djikstra_grid(width, height, g, start):
    min_reach = [[inf for x in range(width)] for y in range(height)]
    reached, reached_completion = [(start, 0)], 0
    reached_set = {start}
    while reached_completion != len(reached):
        (cx, cy), ci = reached[reached_completion]
        reached_completion += 1
        if not g(cx, cy): continue
        if ci < min_reach[cy][cx]: min_reach[cy][cx] = ci
        for nx, ny in (cx+1, cy), (cx-1, cy), (cx, cy-1), (cx, cy+1):
            if (nx, ny) not in reached_set:
                reached.append(((nx, ny), ci + 1))
                reached_set.add((cx, cy))
    return min_reach


def make_passings(l):
    reached, reached_completion = [((0, 0), 0)], 0
    reached_set = {(0, 0)}
    while reached_completion != len(reached):
        (cx, cy), ci = reached[reached_completion]
        reached_completion += 1
        if ci >= l: continue
        for nx, ny in (cx+1, cy), (cx-1, cy), (cx, cy-1), (cx, cy+1):
            if (nx, ny) not in reached_set:
                reached.append(((nx, ny), ci + 1))
                reached_set.add((nx, ny))
    return reached


ti = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""[1:-1].split("\n")


assert(sol0(ti, 100)) == 0
assert(sol0(ti, 20)) == 5
assert(sol0(ti, 64)) == 1
assert(sol1(ti, 76)) == 3


try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri, 100))
print(sol1(ri, 100))
