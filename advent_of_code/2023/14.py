# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


with open("input.txt") as f:
    inputed = f.read()
get_grid = lambda: [[c for c in l] for l in inputed.split("\n")[:-1]]


def tilt_1(grid, x, y, get_next):
    cx, cy = get_next(x, y)
    sr = 0
    while 0 <= cx < len(grid[0]) and 0 <= cy < len(grid) and grid[cy][cx] != "#":
        if grid[cy][cx] == "O":
            sr += 1
        cx, cy = get_next(cx, cy)
    cx, cy = get_next(x, y)
    for i in range(sr):
        grid[cy][cx] = "O"
        cx, cy = get_next(cx, cy)
    while 0 <= cx < len(grid[0]) and 0 <= cy < len(grid) and grid[cy][cx] != "#":
        if grid[cy][cx] != "#":
            grid[cy][cx] = "."
        cx, cy = get_next(cx, cy)



def tilt_with_first_and_next(grid, get_first, get_next):
    for x, y in get_first(grid):
        tilt_1(grid, x, y, get_next)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                tilt_1(grid, x, y, get_next)


score = lambda grid: sum(sum(1 for c in l if c == "O") * (i + 1) for i, l in enumerate(reversed(grid)))


dirs = (
    (lambda grid: ((x,           -1) for x in range(len(grid[0]))), lambda x, y: (x, y + 1)),
    (lambda grid: ((-1,           y) for y in range(len(grid   ))), lambda x, y: (x + 1, y)),
    (lambda grid: ((x,    len(grid)) for x in range(len(grid[0]))), lambda x, y: (x, y - 1)),
    (lambda grid: ((len(grid[0]), y) for y in range(len(grid   ))), lambda x, y: (x - 1, y)),
)


grid = get_grid()
tilt_with_first_and_next(grid, *dirs[0])
print(score(grid))


# Test from part 2
tgi = (
    "O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\n"
    "O.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#...."
)
tgo1 = (
    ".....#....\n....#...O#\n...OO##...\n.OO#......\n.....OOO#.\n"
    ".O#...O#.#\n....O#....\n......OOOO\n#...O###..\n#..OO#...."
)
tgo2 = (
    ".....#....\n....#...O#\n.....##...\n..O#......\n.....OOO#.\n"
    ".O#...O#.#\n....O#...O\n.......OOO\n#..OO###..\n#.OOO#...O"
)
tgo3 = (
    ".....#....\n....#...O#\n.....##...\n..O#......\n.....OOO#.\n"
    ".O#...O#.#\n....O#...O\n.......OOO\n#...O###.O\n#.OOO#...O"
)
tg = [[c for c in l] for l in tgi.split("\n")]
for tgo in (tgo1, tgo2, tgo3):
    for d in dirs:
        tilt_with_first_and_next(tg, *d)
    assert tg == [[c for c in l] for l in tgo.split("\n")]


# Part 2
real_target = 1000000000
grid = get_grid()
r = {}
for i in range(real_target):
    current = "".join(c for l in grid for c in l)
    if current in r:
        base, repetition = r[current], i
        break
    r[current] = i
    for d in dirs:
        tilt_with_first_and_next(grid, *d)
first_target = (real_target - base) % (repetition - base) + base
regrid = lambda s: [[s[y * len(grid[0]) + x] for x in range(len(grid[0]))] for y in range(len(grid))]
print(score(next(regrid(k) for k, v in r.items() if v == first_target)))
