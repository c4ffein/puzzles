# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

with open("input.txt") as f:
    i = f.read()[:-1]


ll = [int(s[ :5]) for s in i.split("\n")]
lr = [int(s[-5:]) for s in i.split("\n")]
s = sum([abs(a-b) for a, b in zip(sorted(ll), sorted(lr))])
print(s)


print(sum((sum(x for y in lr if x == y)) for x in ll))
