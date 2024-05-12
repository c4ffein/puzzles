with open("input.txt") as f:
    i = f.read()
grids = [s.split("\n") for s in i.split("\n\n")]
del grids[-1][-1]


def score_y(grid):
    for i in range(len(grid) - 1):
        if all(l0 == l1 for l0, l1 in zip(grid[i::-1], grid[i+1:])):
            return i + 1
    return 0


def score_y_2(grid):
    r = 0
    for i in range(len(grid) - 1):
        sl = None
        for l0, l1 in zip(grid[i::-1], grid[i+1:]):
            if l0 != l1:
                if sl is not None:
                    break
                sl = (l0, l1)
        else:
            if sl is None:
                continue
            if sum(1 for c0, c1 in zip(*sl) if c0 != c1) == 1:
                return i + 1
    return 0


score = lambda grid: 100 * score_y(grid) + score_y([*zip(*grid[::-1])])
score_2 = lambda grid: 100 * score_y_2(grid) + score_y_2([*zip(*grid[::-1])])


print(sum(score(grid) for grid in grids))
print(sum(score_2(grid) for grid in grids))
