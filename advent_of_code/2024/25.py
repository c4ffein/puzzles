# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from pprint import pprint as pp


def load(ci):
    inputs = [
        (all(c == "#" for c in cg[0]), [sum(1 for v in c if v == "#") for c in zip(*cg)])
        for cg in
        [g.split("\n") for g in ci.split("\n\n")]
    ]
    return [i for is_key, i in inputs if is_key], [i for is_key, i in inputs if not is_key], 7  # 7 is cheese


def sol0(ci):
    keys, locks, height = load(ci)
    return sum(1 for k in keys for l in locks if all(a + b <= height for a, b in zip(k, l)))


def sol1(ci):
    pass



ti = """
#####\n.####\n.####\n.####\n.#.#.\n.#...\n.....\n
#####\n##.##\n.#.##\n...##\n...#.\n...#.\n.....\n
.....\n#....\n#....\n#...#\n#.#.#\n#.###\n#####\n
.....\n.....\n#.#..\n###..\n###.#\n###.#\n#####\n
.....\n.....\n.....\n#....\n#.#..\n#.#.#\n#####
"""[1:-1]


assert(sol0(ti)) == 3
assert(sol1(ti)) == None


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
