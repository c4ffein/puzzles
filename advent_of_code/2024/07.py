# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

ti = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".split("\n")[1:-1]


def sol0(ci):
    ci = [(int(l[0]), [int(v) for v in l[1].split(" ")]) for l in [l.split(": ") for l in ci]]
    return sum(soll0(*l) for l in ci)


def soll0(iv, l):
    for i in range(2 ** (len(l)-1)):
        ops = [v == "1" for v in bin(i)[2:].zfill(len(l)-1)]
        c = l[0]
        for op, v in zip(ops, l[1:]):
            c = c*v if op else c+v
        if c == iv:
            return iv
    return 0


def sol1(ci):
    ci = [(int(l[0]), [int(v) for v in l[1].split(" ")]) for l in [l.split(": ") for l in ci]]
    return sum(soll1(*l) for l in ci)


def soll1(iv, l):
    for i in range(3 ** (len(l)-1)):
        c = l[0]
        for v in l[1:]:
            c = c*v if i % 3 == 0 else c+v if i % 3 == 1 else int(str(c) + str(v))
            i //= 3
        if c == iv:
            return iv
    return 0


assert sol0(ti) == 3749
assert sol1(ti) == 11387

with open("input.txt") as f:
    ri = f.read().split("\n")[:-1]


print(sol0(ri))
print(sol1(ri))
