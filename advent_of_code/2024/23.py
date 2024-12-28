# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from pprint import pprint as pp


def mg(ci):
    nodes = {}
    for a, b in [v.split("-") for v in ci]:
        if a not in nodes: nodes[a] = set()
        if b not in nodes: nodes[b] = set()
        nodes[a].add(b)
        nodes[b].add(a)
    return nodes


def make_trios(nodes):
    return {
        tuple(sorted([b_node, n_node, v_node]))
        for b_node, b_neighs in nodes.items()
        for n_node in b_neighs
        for v_node in nodes[n_node]
        if v_node in b_neighs
    }


def sol0(ci):
    return len([t for t in make_trios(mg(ci)) if any(c[0] == "t" for c in t)])


def sol1(ci):
    nodes = mg(ci)
    n_groups = [None, None, None, make_trios(nodes)]
    i = 3
    while True:
        n_groups.append(set())
        for group in n_groups[i]:
            neighs = set(v for n in group for v in nodes[n] if v not in group)
            for neigh in neighs:
                if all(neigh in nodes[node] for node in group):
                    n_groups[i+1].add(tuple(sorted([*group, neigh])))
        if len(n_groups[i+1]) == 0:
            return ",".join(next(iter(n_groups[i])))
        i += 1


ti = """
kh-tc; qp-kh; de-cg; ka-co; yn-aq; qp-ub; cg-tb; vc-aq; tb-ka; wh-tc; yn-cg; kh-ub; ta-co; de-co; tc-td; tb-wq; 
wh-td; ta-ka; td-qp; aq-cg; wq-ub; ub-vc; de-ta; wq-aq; wq-vc; wh-yn; ka-de; kh-ta; co-tc; wh-qp; tb-vc; td-yn
""".replace("\n", "").replace(" ", "").split(";")


assert(sol0(ti)) == 7
assert(sol1(ti)) == "co,de,ka,ta"


try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
