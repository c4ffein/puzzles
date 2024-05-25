# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


from collections import namedtuple
from enum import Enum
from itertools import chain


with open("input.txt") as f:
    input_file = f.read()


grid = input_file.split("\n")[:-1]
test_grid = (
    ".|...\\....\n|.-.\\.....\n.....|-...\n........|.\n..........\n"
    ".........\\\n..../.\\\\..\n.-.-/..|..\n.|....-|.\\\n..//.|...."
).split("\n")


Direction = Enum("Direction", ["UP", "DOWN", "LEFT", "RIGHT"], start = 0)
DirectionInfo = namedtuple("DirectionInfo", (e.name for e in Direction), defaults=(False,) * len(Direction))
opposites = DirectionInfo(*(e.value for e in [Direction.DOWN, Direction.UP, Direction.RIGHT, Direction.LEFT]))
_t = lambda *args: DirectionInfo(*(bool(e) for e in args))
cases_op = {
    "." : DirectionInfo(_t(0, 1, 0, 0), _t(1, 0, 0, 0), _t(0, 0, 0, 1), _t(0, 0, 1, 0)),
    "/" : DirectionInfo(_t(0, 0, 1, 0), _t(0, 0, 0, 1), _t(1, 0, 0, 0), _t(0, 1, 0, 0)),
    "\\": DirectionInfo(_t(0, 0, 0, 1), _t(0, 0, 1, 0), _t(0, 1, 0, 0), _t(1, 0, 0, 0)),
    "-" : DirectionInfo(_t(0, 0, 1, 1), _t(0, 0, 1, 1), _t(0, 0, 0, 1), _t(0, 0, 1, 0)),
    "|" : DirectionInfo(_t(0, 1, 0, 0), _t(1, 0, 0, 0), _t(1, 1, 0, 0), _t(1, 1, 0, 0)),
}
direction_taker = DirectionInfo(
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
)



def lighted_boxes(grid, starter=(0, 0, Direction.LEFT.value)):
    lighted = [[_t(0, 0, 0, 0) for _ in line] for line in grid]
    to_treat = [starter]
    while to_treat:
        x, y, coming_from = to_treat.pop()
        if lighted[y][x][coming_from]:
            continue
        lighted[y][x] = DirectionInfo(*((i == coming_from or e) for i, e in enumerate(lighted[y][x])))
        for going_to, actually_going in enumerate(cases_op[grid[y][x]][coming_from]):
            if not actually_going:
                continue
            nx, ny = direction_taker[going_to](x, y)
            if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
                continue
            to_treat.append((nx, ny, opposites[going_to]))
    return lighted


assert "\n".join(("".join("#" if any(c) else "." for c in l)) for l in lighted_boxes(test_grid)) == (
    "######....\n.#...#....\n.#...#####\n.#...##...\n.#...##...\n"
    ".#...##...\n.#..####..\n########..\n.#######..\n.#...#.#.."
)


score = lambda lighted_grid: sum(1 for l in lighted_grid for c in l if any(c))
print(score(lighted_boxes(grid)))
r = 0
print(f"\ntesting {len(grid) * 2 + len(grid[0]) * 2} cases")
for starter in chain (
    ((x,                0, Direction.UP.value   ) for x in range(len(grid[0]))),
    ((x,    len(grid) - 1, Direction.DOWN.value ) for x in range(len(grid[0]))),
    ((0,                y, Direction.LEFT.value ) for y in range(len(grid   ))),
    ((len(grid[0]) - 1, y, Direction.RIGHT.value) for y in range(len(grid   ))),
):
    print("#", end="", flush=True)
    r = max(r, score(lighted_boxes(grid, starter=starter)))
print("\n")
print(r)
