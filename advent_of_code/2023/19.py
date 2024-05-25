# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


with open("input.txt") as f:
    input_str = f.read()


def get_workflows_and_pieces(input_str):
    workflows_str, ratings_str = input_str.split("\n\n")
    swork = lambda s: [(int(e) if i == 2 else e) for i, e in enumerate([
        ss
        for e in (
            [s.split("<")[0], "<", s.split("<")[1]]
            if "<" in s
            else [s.split(">")[0], ">", s.split(">")[1]]
            if ">" in s
            else [s]
        )
        for ss in e.split(":")
    ])]
    workflows = {
        k: [swork(nv) for nv in (v[:-1].split(","))] for k, v in (w.split("{") for w in workflows_str.split("\n"))
    }
    pieces = [{k: int(v) for k, v in [s.split("=") for s in r[1:-1].split(",")]} for r in ratings_str.split("\n")[:-1]]
    return workflows, pieces


def solve_1(input_str):
    workflows, pieces = get_workflows_and_pieces(input_str)
    accepted = []
    rejected = []
    for piece in pieces:
        current = "in"
        while True:
            if current == "A":
                accepted.append(piece)
                break
            if current == "R":
                rejected.append(piece)
                break
            for r in workflows[current]:
                if len(r) == 1:
                    [current] = r
                    break
                if (r[1] == "<" and piece[r[0]] < r[2]) or (r[1] == ">" and piece[r[0]] > r[2]):
                    current = r[3]
                    break
    return sum(sum(p.values()) for p in accepted)


def solve_2(input_str):
    workflows, _ = get_workflows_and_pieces(input_str)

    def valids(state, index=0, x=(1, 4001), m=(1, 4001), a=(1, 4001), s=(1, 4001)):
        if state == "R":
            return 0
        if state == "A":
            r = 1
            for min_, max_ in (x, m, a, s):
                r *= max_ - min_
            return r
        ws = workflows[state]
        if index + 1 == len(ws):
            return valids(ws[index][0], 0, x, m, a, s)
        letter, sign, limit, dest = ws[index]
        st0 = {k: v for k, v in zip("xmas", (x, m, a, s))}
        st1 = {**st0}
        if sign == "<":
            st0[letter] = (st0[letter][0], min(st0[letter][1], limit))
            st1[letter] = (max(st1[letter][0], limit), st1[letter][1])
        else:
            st0[letter] = (max(st0[letter][0], limit + 1), st0[letter][1])
            st1[letter] = (st1[letter][0], min(st1[letter][1], limit + 1))
        return sum([
            (valids(dest,  0,         **st0) if st0[letter][0] < st0[letter][1] else 0),
            (valids(state, index + 1, **st1) if st1[letter][0] < st1[letter][1] else 0),
        ])

    return valids("in")


print(solve_1(input_str))
print(solve_2(input_str))
