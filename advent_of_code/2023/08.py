# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


from itertools import cycle, count
from math import gcd


def lcm(numbers):
    r = 1
    for n in numbers:
        r = r * n // gcd(r, n)
    return r


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]
table = {l[:3]: (l[7:10], l[12:15]) for l in ls[2:]}


# V1
instructions = cycle(ls[0])
current = "AAA"
for i in count(1):
    current = table[current][0 if next(instructions) == "L" else 1]
    if current == "ZZZ":
        print(i)
        break


# V2
initials = [e for e in table if e.endswith("A")]
loop_starts = [0] * len(initials)
loop_ends = [0] * len(initials)
instructions_list = ls[0]
valids = [[] for _ in initials]
for ghost_id, (valids_position_for_ghost, initial) in enumerate(zip(valids, initials)):
    # Step 1 - Find loops starts and ends
    instructions = cycle(instructions_list)
    current = initial
    starts = {}
    for i in count(0):
        if i % len(instructions_list) == 0:
            if current not in starts:
                starts[current] = i
            else:
                loop_starts[ghost_id] = starts[current]
                loop_ends[ghost_id] = i
                break
        current = table[current][0 if next(instructions) == "L" else 1]
    # Step 2 - Useless computation, just shows valids == loop_lens
    # instructions = cycle(instructions_list)
    # current = initial
    # for i in range(loop_ends[ghost_id]):
    #     if current.endswith("Z"):
    #         valids_position_for_ghost.append(i)
    #     current = table[current][0 if next(instructions) == "L" else 1]


loop_lens = [loop_end - loop_start for loop_end, loop_start in zip(loop_ends, loop_starts)]
# valids = [valid[0] for valid in valids]
# valids_in_loops = [valid - loop_start for valid, loop_start in zip(valids, loop_starts)]
# print(loop_starts)
# print(loop_ends)
# print(loop_lens)
# print(valids)
# print(valids_in_loops)
# print([loop_len - valid_in_loop for loop_len, valid_in_loop in zip(loop_lens, valids_in_loops)])
# Just figured out the last computation was equal to loop_starts, so...
print(lcm(loop_lens))
