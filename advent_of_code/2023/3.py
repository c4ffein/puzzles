# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]


parts = []
for j, l in enumerate(ls):
    in_part = False
    for i, c in enumerate(l):
        if in_part:
            if c not in "0123456789":
                parts[-1].append(i)
                in_part = False
        elif c in "0123456789":
            parts.append([j, i])
            in_part = True
    if in_part:
        parts[-1].append(i+1)


get_char = lambda matrix, x, y: (
    "."
    if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0])
    else matrix[y][x]
)


is_part_valid = lambda j, i0, i1: any(
    get_char(ls, x, y) not in "0123456789."
    for ci in range(i0-1, i1+1)
    for x, y in ((ci, j - 1), (ci, j), (ci, j + 1))
)


print(sum(int(ls[j][i0:i1]) for j, i0, i1 in parts if is_part_valid(j, i0, i1)))
r = 0
for x, y in ((x, y) for x in range(len(ls[0])) for y in range(len(ls)) if ls[y][x] == "*"):
    adjacent_parts = [p for p in parts if p[0] in [y-1, y, y+1] and p[1] <= x + 1 and p[2] >= x]
    if len(adjacent_parts) != 2:
        continue
    (y0, xs0, xe0), (y1, xs1, xe1) = adjacent_parts
    r += int(ls[y0][xs0:xe0]) * int(ls[y1][xs1:xe1])
print(r)
