# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

ti = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""[1:-1].split("\n")


from enum import Enum
Dir = Enum("Dir", "up right down left")
ppt = [Dir.up, Dir.right, Dir.down, Dir.left, Dir.up]
next_direction = lambda p: ppt[ppt.index(p) + 1]


def sol0(ci):
    return len(sol0_b(ci))

def sol0_b(ci):
    g = [[c == "#" for c in l] for l in ci]
    sy = [i for i, l in enumerate(ci) if "^" in l][0]
    sx = [i for i, c in enumerate(ci[sy]) if c == "^"][0]
    cp = (sx, sy)
    traversed = set()
    direction = Dir.up
    while 0 <= cp[0] < len(g[0]) and 0 <= cp[1] < len(g):
        traversed.add(cp)
        np = next_move(cp, direction)
        if not (0 <= np[0] < len(g[0]) and 0 <= np[1] < len(g)):
            break
        if g[np[1]][np[0]]:
            direction = next_direction(direction)
            continue
        cp = np
    return traversed


def next_move(position, direction):
    if direction == Dir.up:    return (position[0]    , position[1] - 1)
    if direction == Dir.down:  return (position[0]    , position[1] + 1)
    if direction == Dir.left:  return (position[0] - 1, position[1]    )
    if direction == Dir.right: return (position[0] + 1, position[1]    )


def sol1(ci):
    r = 0
    sy = [i for i, l in enumerate(ci) if "^" in l][0]
    sx = [i for i, c in enumerate(ci[sy]) if c == "^"][0]
    cp = (sx, sy)
    path = sol0_b(ci)
    for i, (x, y) in enumerate(path):
        if i % 100 == 0: print(f"{str(i).rjust(7)} / {len(path)}")
        if ci[y][x] == "^":
            continue
        g = [[c == "#" for c in l] for l in ci]
        g[y][x] = True
        if sol1_b(g, cp):
            r += 1
    return r


def sol1_b(g, cp):
    direction = Dir.up
    traversed = set()
    while 0 <= cp[0] < len(g[0]) and 0 <= cp[1] < len(g):
        if (*cp, direction.value) in traversed:
            return True
        traversed.add((*cp, direction.value))
        np = next_move(cp, direction)
        if not (0 <= np[0] < len(g[0]) and 0 <= np[1] < len(g)):
            break
        if g[np[1]][np[0]]:
            direction = next_direction(direction)
            continue
        cp = np
    return False


assert sol0(ti) == 41
assert sol1_b([[c == "#" for c in l] for l in ti], (4, 6)) == False
assert sol1(ti) == 6


with open("input.txt") as f:
    ri = f.read().split("\n")[:-1]


print(sol0(ri))
print(sol1(ri))
