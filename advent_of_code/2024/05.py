# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

ti = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""[1:-1]



def sol0(si):
    p0, p1 = si.split("\n\n")
    ands = [(int(x[0]), int(x[1])) for x in (b.split("|") for b in p0.split("\n"))]
    lists = [[int(v) for v in x] for x in (b.split(",") for b in p1.split("\n"))]

    r = 0
    for l in lists:
        for r0, r1 in ands:
            if r0 in l and r1 in l and l.index(r0) > l.index(r1):
                break
        else:
            r += l[len(l) // 2]
    return r


def sol1(si):
    p0, p1 = si.split("\n\n")
    ands = [(int(x[0]), int(x[1])) for x in (b.split("|") for b in p0.split("\n"))]
    lists = [[int(v) for v in x] for x in (b.split(",") for b in p1.split("\n"))]

    r = 0
    for l in lists:
        for r0, r1 in ands:
            if r0 in l and r1 in l and l.index(r0) > l.index(r1):
                nnv = sl1(ands, l)
                r += nnv
                break
    return r

def sl1(ands, l):
    ordered = order([a for a in ands if a[0] in l and a[1] in l])
    sordered = set(ordered)
    nl = []
    for e in l:
        if e not in sordered:
            nl.append(e)
            continue
        nl.append(ordered[0])
        ordered = ordered[1:]
    return nl[len(nl) // 2]


def order(ands):
    if len(ands) == 0:
        return []
    if len(ands) == 1:
        return [ands[0][0], ands[0][1]]
    sands = set(a[0] for a in ands) | set(a[1] for a in ands)
    ss = ([v for v in sands if v not in [a[1] for a in ands]])
    if len(ss) != 1:
        raise Exception(f"ONO {ss} {ands}")
    s = ss[0]
    return [s] + order([p for p in ands if p[0] != s and p[1] != s])


assert sol0(ti) == 143
assert sol1(ti) == 123


with open("input.txt") as f:
    fi = f.read()[:-1]


print(sol0(fi))
print(sol1(fi))
