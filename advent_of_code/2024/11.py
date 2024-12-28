# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

def sol0(ci):
    return sum(optimized_blink(v, 25) for v in ci)
    r = ci
    for i in range(25):
        r = blink(r)
        print(i+1, ": ", len(r))
    return len(r)


def sol1(ci):
    return sum(optimized_blink(v, 75) for v in ci)


def blink(arr):
    return [
        o
        for i in arr
        for o in (
            [1]
            if i == 0
            else [int(str(i)[:len(str(i)) // 2]), int(str(i)[len(str(i)) // 2:])]
            if len(str(i)) % 2 == 0
            else [i * 2024]
        )
    ]


saveds = {}  # {(value, number_of_blinks_remainings): result}


def optimized_blink(v, n):
    if n == 0:
        return 1
    if (v, n) in saveds:
        return saveds[(v, n)]
    s = str(v)
    if v == 0:
        r = optimized_blink(1, n-1)
    elif len(str(v)) % 2 == 0:
        r = optimized_blink(int(s[:len(s) // 2]), n-1) + optimized_blink(int(s[len(s) // 2:]), n-1)
    else:
        r = optimized_blink(v * 2024, n-1)
    saveds[(v, n)] = r
    return r


tti = """
125 17
253000 1 7
253 0 2024 14168
512072 1 20 24 28676032
512 72 2024 2 0 2 4 2867 6032
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
""".split("\n")[1:-1]
tti = [[int(v) for v in l.split(" ")] for l in tti]
for l0, l1 in zip(tti[:-1], tti[1:]):
    assert blink(l0) == l1


ti = [int(v) for v in """125 17""".split(" ")]


assert sol0(ti) == 55312
assert optimized_blink(ti[0], 25) + optimized_blink(ti[1], 25) == 55312


try:
    with open("input.txt") as f:
        ri = [int(v) for v in f.read()[:-1].split(" ")]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
