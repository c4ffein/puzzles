# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf

ti = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
ti2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def sol(inp):
    r = 0
    for ri in [inp[i:] for i in range(len(inp))]:
        if ri[:4] != "mul(": continue
        a, b = "", ""
        for ci, c in enumerate(ri[4:]):
            if c == ",": break
            elif c in "0123456789": a += c
            else: break
        if c != "," or not a: continue
        a = int(a)
        bci = ci + 5
        for ci, c in enumerate(ri[bci:]):
            if c == ")": break
            if c in "0123456789": b += c
            else: break
        if c != ")" or not b: continue
        b = int(b)
        r += a * b
    return  r

def sol2(inp):
    enabled = True
    r = 0
    for ri in [inp[i:] for i in range(len(inp))]:
        if ri.startswith("do()"):
            enabled = True
            continue
        if ri.startswith("don't()"):
            enabled = False
            continue
        if not enabled:
            continue
        if ri[:4] != "mul(":
            continue
        a, b = "", ""
        for ci, c in enumerate(ri[4:]):
            if c == ",": break
            elif c in "0123456789": a += c
            else: break
        if c != "," or not a: continue
        a = int(a)
        bci = ci + 5
        for ci, c in enumerate(ri[bci:]):
            if c == ")": break
            if c in "0123456789": b += c
            else: break
        if c != ")" or not b: continue
        b = int(b)
        r += a * b
    return  r

assert sol(ti) == 161
assert sol2(ti2) == 48

with open("input.txt") as f:
    in_s = f.read()

print(sol(in_s))
print(sol2(in_s))
