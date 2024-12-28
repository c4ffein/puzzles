# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf


dirs = {
    "^": (lambda x, y: (x, y-1)),
    "v": (lambda x, y: (x, y+1)),
    "<": (lambda x, y: (x-1, y)),
    ">": (lambda x, y: (x+1, y)),
}


connecteds_from_rock = {  # from left of rock
    "^": (lambda x, y: ((x, y-1), (x+1, y-1))),
    "v": (lambda x, y: ((x, y+1), (x+1, y+1))),
    "<": (lambda x, y: ((x-1, y),)),
    ">": (lambda x, y: ((x+2, y),)),
}


def sol0(ci):
    grid, dirs = cons(ci)
    player = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "@"][0]
    for dir in dirs:
        player = move(grid, player, dir)
    print(printable_grid(grid))
    return sum((100 * y + x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "O")


def sol1(ci):
    grid, dirs = cons(ci)
    grid = new_grid(grid)
    player = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "@"][0]
    for dir in dirs:
        player = nmove(grid, player, dir)
    return sum((100 * y + x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "[")


def cons(ci):
    grid, dirs = ci.split("\n\n")
    grid = [[c for c in l] for l in grid.split("\n")]
    dirs = dirs.replace("\n", "")
    return grid, dirs


def new_grid(g):
    return [
        [
            c if c == "#" else "[]"[i] if c == "O" else "@" if c == "@" and i == 0 else "."
            for c in l for i in [0, 1]
        ]
        for l in g
    ]


def nmove(grid, player, direction):
    current = player
    current = dirs[direction](*current)
    stone_pos = lambda x, y: ((x, y) if grid[y][x] == "[" else (x-1, y))
    is_stone = lambda x, y: grid[y][x] in "[]"
    if grid[current[1]][current[0]] == "#":
        return player
    stones_to_add_to_connected = set()
    connected_stones = set()
    if is_stone(current[0], current[1]):
        stones_to_add_to_connected.add(stone_pos(*current))
    while stones_to_add_to_connected:
        current_stone = stones_to_add_to_connected.pop()
        connected_stones.add(current_stone)
        for next_pos in connecteds_from_rock[direction](*current_stone):
            if grid[next_pos[1]][next_pos[0]] == "#":
                return player
            if is_stone(*next_pos) and stone_pos(*next_pos) not in connected_stones:
                stones_to_add_to_connected.add(stone_pos(*next_pos))
    for x, y in connected_stones:
        grid[y][x], grid[y][x+1] = ".", "."
    for x, y in connected_stones:
        nx, ny = dirs[direction](x, y)
        grid[ny][nx], grid[ny][nx+1] = "[", "]"
    grid[player[1]][player[0]] = "."
    grid[current[1]][current[0]] = "."
    return current


def move(grid, player, direction):
    current = player
    current = dirs[direction](*current)
    buffer = []
    while grid[current[1]][current[0]] not in "#.":
        buffer.append(current)
        current = dirs[direction](*current)
    if grid[current[1]][current[0]] == "#":
        return player
    if len(buffer) == 0:
        grid[current[1]][current[0]] = "@"
        grid[player[1]][player[0]] = "."
        return current[0], current[1]
    grid[current[1]][current[0]] = "O"
    grid[buffer[0][1]][buffer[0][0]] = "@"
    grid[player[1]][player[0]] = "."
    return buffer[0][0], buffer[0][1]


def printable_grid(grid):
    return "\n" + "\n".join("".join(c for c in l) for l in grid) + "\n"


ti = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""[1:-1]


assert(sol0(ti)) == 10092
assert(sol1(ti)) == 9021


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
