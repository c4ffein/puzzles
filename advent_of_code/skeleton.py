# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from sys import exit
from math import inf
from pprint import pprint as pp


def sol0(ci):
    pass


def sol1(ci):
    pass


ti = """
"""[1:-1]


assert(sol0(ti)) == None
assert(sol1(ti)) == None


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    exit(-1)
print(sol0(ri))
print(sol1(ri))
