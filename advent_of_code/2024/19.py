# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf


def sol0(ci):
    towels, patterns = ci[0].split(", "), ci[2:]
    return sum(1 for pattern in patterns if possible(towels, pattern))


def sol1(ci):
    towels, patterns = ci[0].split(", "), ci[2:]
    return sum(score(towels, pattern) for pattern in patterns)


def possible(towels, pattern, cache=None):
    if not pattern:
        return True
    if cache is None: cache = {}
    cached = cache.get(pattern)
    if cached is not None: return cached
    r = any(possible(towels, pattern[len(towel):], cache) for towel in towels if pattern.startswith(towel))
    cache[pattern] = r
    return r


def score(towels, pattern, cache=None):
    if not pattern:
        return 1
    if cache is None: cache = {}
    cached = cache.get(pattern)
    if cached is not None: return cached
    r = sum(score(towels, pattern[len(towel):], cache) for towel in towels if pattern.startswith(towel))
    cache[pattern] = r
    return r



ti = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""[1:-1].split("\n")


assert(sol0(ti)) == 6
assert(sol1(ti)) == 16


try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
