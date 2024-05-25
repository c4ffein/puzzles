# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


from functools import reduce


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]
nls = [[int(n) for n in l.split()] for l in ls]


def oasis_next(arr):
    arrs = [arr]
    while any(e != 0 for e in arrs[-1]):
        arrs.append([b - a for a, b in zip(arrs[-1][:-1], arrs[-1][1:])])
    return sum(arr[-1] for arr in reversed(arrs[:-1]))


def oasis_prev(arr):
    arrs = [arr]
    while any(e != 0 for e in arrs[-1]):
        arrs.append([b - a for a, b in zip(arrs[-1][:-1], arrs[-1][1:])])
    return reduce(lambda a, b: b - a, (arr[0] for arr in reversed(arrs[:-1])))


def test():
    arra = [0,   3,   6,   9,  12,  15]
    arrb = [1,   3,   6,  10,  15,  21]
    arrc = [10,  13 , 16, 21 , 30 , 45]
    assert oasis_next(arra) == 18
    assert oasis_next(arrb) == 28
    assert oasis_next(arrc) == 68
    assert (sum(oasis_next(l) for l in [arra, arrb, arrc])) == 114
    assert oasis_prev(arrc) == 5


test()
print(sum(oasis_next(l) for l in nls))
print(sum(oasis_prev(l) for l in nls))
