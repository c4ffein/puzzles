# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

with open("input.txt") as f:
    i = f.read().split("\n")[:-1]
g = [[int(v) for v in l.split(" ")] for l in i]


def check_l(l):
    return (
        (all((l[i] < l[i+1] <= l[i] + 3) for i in range(len(l)-1)))
        or (all((l[i+1] < l[i] <= (l[i+1] + 3)) for i in range(len(l)-1)))
    )


print(sum(1 for l in g if check_l(l)))
rems = lambda l: [l[:i] + l[i+1:] for i in range(len(l))]
print(sum(1 for l in g if any(check_l(nl) for nl in rems(l))))
