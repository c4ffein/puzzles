# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


with open("input.txt") as f:
    real_input = f.read().split("\n")[:-1]


test_input = (
    "R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\n"
    "U 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)"
).split("\n")


director = {
    "U": lambda x, y, m: (x, y - m),
    "D": lambda x, y, m: (x, y + m),
    "L": lambda x, y, m: (x - m, y),
    "R": lambda x, y, m: (x + m, y),
}


def solve(lines):
    current_pos = (0, 0)
    last_dir = lines[-1][0]
    points = {(0, 0): (None, None)}
    last_pos = (0, 0)
    for direction, long in lines[:-1]:
        current_pos = director[direction](*last_pos, long)
        points[current_pos] = (last_pos, None)
        assert points[last_pos][1] is None
        points[last_pos] = (points[last_pos][0], current_pos)
        last_pos = current_pos
    direction, long = lines[-1]
    assert director[direction](*last_pos, long) == (0, 0)
    assert points[(0, 0)][0] is None
    points[(0, 0)] = (last_pos, points[(0, 0)][1])
    points[last_pos] = (points[last_pos][0], (0, 0))

    verticals = {}  # x: [(top, bottom), ...]
    for pc, (pp, pn) in points.items():
        if pc[0] == pn[0]:
            verticals[pc[0]] = verticals.get(pc[0], [])
            verticals[pc[0]].append((min(pc[1], pn[1]), max(pc[1], pn[1])))
    horizontals = sorted(set(y for _, y in points))
    verticals = {k: v for k, v in sorted(verticals.items())}
    start_x = min(p[0] for p in points)
    end_x = max(p[0] for p in points)
    r = 0

    def calc(l):
        s = 0
        inside = None
        last_is_top = False
        last_is_bottom = False
        for x, top_bottom_array in verticals.items():
            if not any(top <= l <= bottom for top, bottom in top_bottom_array):
                continue
            current_is_top = any(top == l for top, _ in top_bottom_array)
            current_is_bottom = any(l == bottom for _, bottom in top_bottom_array)
            if inside is not None:
                if (current_is_top and last_is_bottom) or (current_is_bottom and last_is_top):
                    last_is_top, last_is_bottom = False, False
                    continue
                if (current_is_top or current_is_bottom) and not (last_is_top or last_is_bottom):
                    last_is_top, last_is_bottom = current_is_bottom, current_is_top  # tricky shit
                    continue
                s += x - inside + 1
                inside = None
            else:
                inside = x
                last_is_top, last_is_bottom = current_is_top, current_is_bottom
        return s

    for cl, nl in zip(horizontals, horizontals[1:]):
        r += calc(cl)
        r += calc(cl + 1) * (nl - cl - 1)
    r += calc(horizontals[-1])
    return r


lines_1 = lambda lines: [(direction, int(length)) for direction, length, _ in (l.split(" ") for l in lines)]
lines_2 = lambda lines: [("RDLU"[int(s[-2])], int(s[2:-2], 16)) for s in (l.split(" ")[-1] for l in lines)]

assert solve(lines_1(test_input)) == 62
print(solve(lines_1(real_input)))
print(solve(lines_2(real_input)))
