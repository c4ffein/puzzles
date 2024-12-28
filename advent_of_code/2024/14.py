# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf


def sol0(ci, width, height):
    ci = consume(ci)
    for i in range(100):
        for p, (vx, vy) in ci:
            p[0] = (p[0] + vx) % width
            p[1] = (p[1] + vy) % height
    q1 = sum(1 for l in ci if l[0][0] < width // 2 and l[0][1] > height // 2)
    q2 = sum(1 for l in ci if l[0][0] > width // 2 and l[0][1] > height // 2)
    q3 = sum(1 for l in ci if l[0][0] < width // 2 and l[0][1] < height // 2)
    q4 = sum(1 for l in ci if l[0][0] > width // 2 and l[0][1] < height // 2)
    return q1 *q2 * q3 * q4


def sol1(ci, width, height):
    guessed_solution = 6511

    ci = consume(ci)
    for i in range(10000):
        for p, (vx, vy) in ci:
            p[0] = (p[0] + vx) % width
            p[1] = (p[1] + vy) % height
        # if i in [22, 125, 47, 148]:  Good row: 22 / 125; Good line: 47 / 148
        # if ((i - 22) % (125 - 22) == 0) and ((i - 47) % (148 - 47) == 0):
        if i == guessed_solution:
            buf = [[any(l[0][0] == x and l[0][1] == y for l in ci) for x in range(width)] for y in range(height)]
            print("\n", i)
            print("\n".join(["".join("X" if c else " " for c in l) for l in buf]))
            print("\n\n")
    return guessed_solution + 1


##  22 / 125 / 47 / 148

def consume(ci):
    return [
        ([int(v) for v in p0[2:].split(",")], (int(p1.split(",")[0][2:]), int(p1.split(",")[1])))
        for p0, p1 in [l.split(" ") for l in ci]
    ]


ti = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""[1:-1].split("\n")


assert(sol0(ti, 11, 7)) == 12


try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri, 101, 103))
print(sol1(ri, 101, 103))
