with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]


lst = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".split("\n")[1:-1]


def compute_grid(grid, added_years):
    x_scores = []
    y_scores = []
    for y, line in enumerate(grid):
        y_scores.append((1 + added_years) if "#" not in line else 1)
    for x, col in ((x, (grid[y][x] for y in range(len(grid)))) for x in range(len(grid[0]))):
        x_scores.append((1 + added_years) if "#" not in col else 1)
    return x_scores, y_scores


def line_distance(scores, d0, d1):
    if d0 > d1:
        d0, d1 = d1, d0
    return sum(scores[d] for d in range(d0, d1))


def distance(x_scores, y_scores, p0, p1):
    return line_distance(x_scores, p0[0], p1[0]) + line_distance(y_scores, p0[1], p1[1])


def compute_path(grid, added_years=1):
    x_scores, y_scores = compute_grid(grid, added_years)
    galaxies = [(x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == "#"]
    return sum(distance(x_scores, y_scores, g0, g1) for i, g0 in enumerate(galaxies) for g1 in galaxies[i + 1:])


x_scores_t = [1, 1, 2, 1, 1, 2, 1, 1, 2, 1]
y_scores_t = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1]
assert distance(x_scores_t, y_scores_t, (3, 0), (7, 8)) == 15
assert compute_path(lst) == 374


print(compute_path(ls))
print(compute_path(ls, added_years=999999))
