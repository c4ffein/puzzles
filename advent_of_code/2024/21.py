# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from itertools import permutations
from pprint import pprint as pp
def assert_equal(x, y):
    if x != y: raise Exception(f"{x} != {y}")

# All move from and to A, except first
_rkf = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
real_keypad_pairs = {  # All possible orderings
    f"{a}{b}": [
        "".join(l)
        for l in set(permutations(max(ja-jb,0) * "<" + max(ib-ia,0) * "v" + max(ia-ib,0) * "^" + max(jb-ja,0) * ">"))
        if (
                (a != "0" or not "".join(l).startswith("<")) and (a != "A" or not "".join(l).startswith("<<"))
            and (b != "0" or not   "".join(l).endswith(">")) and (b != "A" or not   "".join(l).endswith(">>"))
        )
    ]
    for ia, la in enumerate(_rkf) for ja, a in enumerate(la) for ib, lb in enumerate(_rkf) for jb, b in enumerate(lb)
    if a is not None and b is not None
}

middle = {
    "A": {"A": "", "^": "<", "v": "v<,<v", "<": "v<<,<v<", ">": "v"},
    "^": {"A": ">", "^": "", "v": "v", "<": "v<", ">": "v>,>v"},
    "v": {"A": "^>,>^", "^": "^", "v": "", "<": "<", ">": ">"},
    "<": {"A": ">>^,>^>", "^": ">^", "v": ">", "<": "", ">": ">>"},
    ">": {"A": "^", "^": "^<,<^", "v": "<", "<": "<<", ">": ""},
}
middle_pairs = {f"{ka}{kb}": vb.split(",") for ka, va in middle.items() for kb, vb in va.items()}

solvv = lambda ci, limit: (
    min(soli(pp+"A", limit) for pp in real_keypad_pairs[f"A{ci[0]}"])
    + sum(min(soli(pp+"A", limit) for pp in real_keypad_pairs[f"{a}{b}"]) for a, b in zip(ci[:-1], ci[1:]))
)

solvb = lambda b: (
    "" if not b
    else middle_pairs[f"A{b[0]}"][0]+"A" + "".join(middle_pairs[f"{a}{b}"][0]+"A" for a, b in zip(b[:-1], b[1:]))
)


g = lambda s, r, p: r if len(s) <= 0 else g(s[1:], [f"{v}{ps}A" for v in r for ps in middle_pairs[f"{p}{s[0]}"]], s[0])
soli_cache = {}
def soli(b, limit):  # Takes string ending by "A", may be only "A", implies starting position of middle at "A"
    if b == "A": return 1  # Since all on A just one press for all the chain
    if (b, limit) in soli_cache:  return soli_cache[(b, limit)]
    subs = b.split("A")[:-1]
    r = len(solvb(f"{b}")) if limit == 0 else sum(min(soli(cs, limit-1) for cs in g(f"{s}A", [""], "A")) for s in subs)
    soli_cache[(b, limit)] = r
    return r


solvv0 = lambda ci: solvv(ci, 2 - 1)
solvv1 = lambda ci: solvv(ci, 25 - 1)
sol0 = lambda ci: sum(int("".join(c for c in s if c.isnumeric())) * solvv0(s) for s in ci)
sol1 = lambda ci: sum(int("".join(c for c in s if c.isnumeric())) * solvv1(s) for s in ci)

assert_equal(solvv0("029A"), len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"))
assert_equal(solvv0("980A"), len("<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"))
assert_equal(solvv0("179A"), len("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))
assert_equal(solvv0("456A"), len("<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"))
assert_equal(solvv0("379A"), len("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))
assert_equal(sol0(["029A", "980A", "179A", "456A", "379A"]), 126384)

try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
