#!/usr/bin/env python
# https://adventofcode.com/2023/day/10

from functools import reduce


get_loop = lambda arr, c=None, n=None, k=(),cm={v: [c == "1" for c in bin(i)[2:].zfill(4)] for i, v in enumerate(".**-*JL**7F*|")}, w=None, z=None: (((c := next((x, y) for y, l in enumerate(arr) for x, c in enumerate(l) if c == "S") if c is None else c) or True)and next(v for v in (get_loop(arr, c, n, w=lambda m, c: (lambda v: ((m[0] != 1 or v[2]) and (m[0] != -1 or v[3]) and (m[1] != 1 or v[1]) and (m[1] != -1 or v[0]))(cm[c])),z=lambda m, c: m if cm[c][0] == cm[c][1] else (0 if m[0] != 0 else 1 if cm[c][2] else -1, 0 if m[1] != 0 else 1 if cm[c][0] else -1)) for n in ((0, 1), (1, 0), (0, -1), (-1, 0))) if v is not None) if n is None else None if not (0 <= c[0] + n[0] < len(arr[0]) and 0 <= c[1] + n[1] < len(arr)) else (*k, (c[0], c[1])) if arr[c[1]+n[1]][c[0]+n[0]] == "S" else None if not w(n, arr[c[1]+n[1]][c[0]+n[0]]) else get_loop(arr, (c[0]+n[0], c[1]+n[1]), z(n, arr[c[1]+n[1]][c[0]+n[0]]), (*k, c), w=w, z=z))


p2 = lambda arr, o: sum(reduce(lambda a, e: (not a[0] if e == "|" else a[0], a[1] + 1 if a[0] and e == "." else a[1]), "".join(l).replace("-", "").replace("LJ", "").replace("F7", "").replace("L7", "|").replace("FJ", "|"), (False, 0))[1] for l in [[("F" if {o[1], o[-1]} == {(o[0][0]+1, o[0][1]), (o[0][0], o[0][1]+1)} else "J" if {o[1], o[-1]} == {(o[0][0]-1, o[0][1]), (o[0][0], o[0][1]-1)} else "L" if {o[1], o[-1]} == {(o[0][0]+1, o[0][1]), (o[0][0], o[0][1]-1)} else "7" if {o[1], o[-1]} == {(o[0][0]-1, o[0][1]), (o[0][0], o[0][1]+1)} else "-" if {o[1], o[-1]} == {(o[0][0]+1, o[0][1]), (o[0][0]-1, o[0][1])} else "|" if {o[1], o[-1]} == {(o[0][0], o[0][1]+1), (o[0][0], o[0][1]-1)} else "!") if (x, y) == o[0] else c if (x, y) in o else "." for x, c in enumerate(l)] for y, l in enumerate(arr)])


b0 = """
.....
.S-7.
.|.|.
.L-J.
.....
"""[1:-1].split("\n")

b1 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""[1:-1].split("\n")
assert len(get_loop(b0)) // 2 == 4
assert len(get_loop(b1)) // 2 == 8

b2 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""[1:-1].split("\n")

b3 = """
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""[1:-1].split("\n")

b4 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""[1:-1].split("\n")

b5 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""[1:-1].split("\n")

assert p2(b2, get_loop(b2)) ==  4
assert p2(b3, get_loop(b3)) ==  4
assert p2(b4, get_loop(b4)) ==  8
assert p2(b5, get_loop(b5)) == 10


import sys
sys.setrecursionlimit(1000000)
with open("input") as f:
    bf = f.read().split("\n")
print(len(get_loop(bf)) // 2)
print(p2(bf, get_loop(bf)))
