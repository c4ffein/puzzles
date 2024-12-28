# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from itertools import combinations
from math import gcd

ti = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".split("\n")[1:-1]


def sol0(ti):
    height = len(ti)
    width = len(ti)
    poss = {c: set() for l in ti for c in l if c != "."}
    for i, l in enumerate(ti):
        for j, c in enumerate(l):
            if c != ".":
                poss[c].add((i, j))
    echoes = set()
    for pairs in poss.values():
        for pair0, pair1 in combinations(pairs, 2):
            diff0, diff1 = pair0[0] - pair1[0], pair0[1] - pair1[1]
            echoes.add((pair0[0]+diff0, pair0[1]+diff1))
            echoes.add((pair1[0]-diff0, pair1[1]-diff1))
    return sum(1 for p0, p1 in echoes if 0<=p0<height and 0<=p1<width)


def sol1(ti):
    height = len(ti)
    width = len(ti)
    poss = {c: set() for l in ti for c in l if c != "."}
    for i, l in enumerate(ti):
        for j, c in enumerate(l):
            if c != ".":
                poss[c].add((i, j))
    echoes = set()
    for pairs in poss.values():
        for pair0, pair1 in combinations(pairs, 2):
            diffy, diffx = pair0[0] - pair1[0], pair0[1] - pair1[1]
            pgcd = gcd(diffx, diffy)
            diffx, diffy = diffx // pgcd, diffy // pgcd
            py, px = pair0[0], pair0[1]
            while 0<=py<height and 0<=px<width:
                echoes.add((py, px))
                py, px = py + diffy, px + diffx
            py, px = pair0[0], pair0[1]
            while 0<=py<height and 0<=px<width:
                echoes.add((py, px))
                py, px = py - diffy, px - diffx
    return sum(1 for p0, p1 in echoes if 0<=p0<height and 0<=p1<width)



assert sol0(ti) == 14
assert sol1(ti) == 34


with open("input.txt") as f:
    ri = f.read().split("\n")[:-1]


print(sol0(ri))
print(sol1(ri))
