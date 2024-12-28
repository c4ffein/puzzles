# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf


def sol0(ci, width, height, step):
    return solv(mg(ci, width, height), width, height, step)


def sol1(ci, width, height):  # could have iterate on sol0, checking the next block appearing on the path, but...
    g = mg(ci, width, height)
    low, high = 0, width * height
    while low+1 != high:
        mid = (low + high) // 2
        t = solv(g, width, height, mid)
        if t == inf: high = mid
        else: low = mid
    return ci.split("\n")[high-1]


def mg(ci, width, height):
    ci = [(i+1, *(int(v) for v in l.split(","))) for i, l in enumerate(ci.split("\n"))]
    g = [[[*(i for i, cx, cy in ci if cx == x and cy == y), None][0] for x in range(width)] for y in range(height)]
    return lambda i, x, y: (g[y][x] is None or g[y][x] > i) if 0 <= x < width and 0 <= y < height else False


def solv(g, width, height, step):
    start, end = (0, 0), (width, height)
    reached, completed = [[start, 0]], set()
    sg = [[inf for _ in range(width)] for _ in range(height)]
    while reached:
        (x, y), ci = reached[0]
        reached = reached[1:]
        if g(step, x, y) and ci < sg[y][x]: sg[y][x] = ci
        completed.add((x, y))
        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if g(step, x, y) and (nx, ny) not in completed and (nx, ny) not in (p for p, _ in reached):
                reached.append(((nx, ny), ci+1))
    return sg[height-1][width-1]


ti = """
5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1\n1,2
5,5\n2,5\n6,5\n1,4\n0,4\n6,4\n1,1\n6,1\n1,0\n0,5\n1,6\n2,0
"""[1:-1]


assert(sol0(ti, 7, 7, 12)) == 22
assert(sol1(ti, 7, 7)) == "6,1"


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri, 71, 71, 1024))
print(sol1(ri, 71, 71))
