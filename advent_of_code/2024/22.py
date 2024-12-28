# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from pprint import pprint as pp


step_0 = lambda s: ((s * 64) ^ s) % 16777216
step_1 = lambda s: ((s // 32) ^ s) % 16777216
step_2 = lambda s: ((s * 2048) ^ s) % 16777216
next_s = lambda i: step_2(step_1(step_0(i)))

def solb0(ci):
    r = ci
    for _ in range(2000): r = next_s(r)
    return r


sol0 = lambda sa: sum(solb0(int(s)) for s in sa)


def sol1(sa):
    lines_ds = []
    all_4_chains = set()
    for start in sa:
        cur = int(start)
        line_ds = {}
        line = [cur % 10]
        for _ in range(2000):
            cur = next_s(cur)
            line.append(cur % 10)
            if len(line) > 4:
                changes = tuple((b-a) for a, b in zip(line[-5:-1], line[-4:]))
                if changes in line_ds: continue
                line_ds[changes] = cur % 10
                all_4_chains.add(changes)
        lines_ds.append(line_ds)
    return max(sum(line_ds.get(chain, 0) for line_ds in lines_ds) for chain in all_4_chains)


ti = """
123;  15887950;  16495136;  527345;  704524;  1553684;  12683156;  11100544;  12249484;  7753432;  5908254
"""[1:-1].split(";  ");  
for sa, sb in zip(ti[:-1], ti[1:]):
    assert next_s(int(sa)) == int(sb)

ti2 = "1: 8685429;  10: 4700978;  100: 15273692;  2024: 8667524".split(";  ")
for l in ti2:
    assert solb0(int(l.split(": ")[0])) == int(l.split(": ")[1])

tis1 = [1, 2, 3, 2024]
assert(sol1(tis1)) == 23


try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
