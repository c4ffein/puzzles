# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


# Tried to solve mainly with lambdas and oneliners, just for fun


from functools import reduce


p1 = lambda a: [
    (lambda l, r, ql: sum(
        1
        for i in range(pow(2, ql))
        if reduce(
            lambda a, b: (b == "#",  a[1] if b == "." else [*a[1][:-1], a[1][-1]+1] if a[0] else [*a[1], 1]),
            (lambda g: [c if c != "?" else next(g) for c in l])(
                "." if c == "0" else "#" for c in bin(i)[2:].zfill(ql)
            ),
            (False, [])
        )[1] == r
    ))(
        l.split(" ")[0],
        [int(i) for i in l.split(" ")[1].split(",")],
        sum(1 for c in l if c == "?")
    )
    for l in a
]

p2 = lambda a: [*(5 * l.split(" ")[0] + " " + ",".join((l.split(" ")[1] for _ in range(5))) for l in a)]


pl1 = lambda s, r, i=0:  print("c", s, r, i) or (  # string, remaining to fill, current index
    ((print("!") or 1) if i < len(s) and all(c == "?" or c == "." for c in s[i:]) else (print("?") or 0))
    if r == []
    else (print("ONN") or 0)
    if i + sum(r) + len(r) - 1 > len(s)
    else pl1(s, r, i + 1)
    if s[i] == "."
    else (
        print("BXX") or 0
        if not all(c == "?" or c == "#" for c in s[i:i+r[0]])
        else print("BGG") or 1
        if len(r) == 1 and i + r[0] == len(s)
        else print("BYY") or 0
        if i + r[0] < len(s) and s[i+r[0]] not in "?."
        else pl1(s, r[1:], i=i+r[0]+1)
    )
    if s[i] == "#"
    else (
        print("XX") or 0
        if not all(c == "?" or c == "#" for c in s[i:i+r[0]])
        else print("GG") or 1
        if len(r) == 1 and i + r[0] == len(s)
        else print("YY") or 0
        if i + r[0] < len(s) and s[i+r[0]] not in "?."
        else pl1(s, r[1:], i=i+r[0]+1)
    ) + (
        pl1(s, r, i + 1)
    )
)


pl = lambda s, r, i=0, p=False: (
    (1 if r == [] or r == [0] else 0)
    if i == len(s)
    else (
        pl(s, r, i=i+1, p=False)
        if s[i] == "."
        else (
            pl(s, [r[0]-1, *r[1:]], i=i+1, p=True)
            if len(r) >= 1
            else 0
        )
        if s[i] == "#"
        else (
            pl(s, [r[0]-1, *r[1:]], i=i+1, p=True)
            if len(r) >= 1
            else 0
        ) + pl(s, r, i=i+1, p=False)
    )
    if not p
    else (
        (pl(s, r[1:], i=i+1, p=False) if r[0] == 0 else 0)
        if s[i] == "."
        else (pl(s, [r[0]-1, *r[1:]], i=i+1, p=True) if r[0] > 0 else 0)
        if s[i] == "#"
        else (
            pl(s, r[1:], i=i+1, p=False) if r[0] == 0 else 0
        ) + (
            pl(s, [r[0]-1, *r[1:]], i=i+1, p=True) if r[0] > 0 else 0
        )
    )
)


p1 = lambda a: [pl(l.split(" ")[0], [int(v) for v in l.split(" ")[1].split(",")]) for l in a]
p2 = lambda a: [pl(l.split(" ")[0] * 5, [int(v) for v in l.split(" ")[1].split(",")] * 5) for l in a]
p2 = lambda a: [print(pl(l.split(" ")[0] * 5, [int(v) for v in l.split(" ")[1].split(",")] * 5)) for l in a]

i = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""[1:-1].split("\n")

assert p1(i) == [1, 4, 1, 1, 4, 10]

with open("input") as f:
    fr = f.read()

print(sum(p1(fr.split("\n")[:-1])))
print(sum(p2(fr.split("\n")[:-1])))
