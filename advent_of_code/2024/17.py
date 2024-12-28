# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf


def read(ci):
    rs, pr = ci.split("\n\n")
    return [int(l[12:]) for l in rs.split("\n")], [int(v) for v in pr[9:].split(",")]


def sol0(ci):
    return ",".join(str(i) for i in solv(*read(ci)))


def solv(registers, program):
    r, ip = [], 0
    while 0 <= ip < len(program):
        literal_operand = program[ip + 1]
        combo_operand = literal_operand if literal_operand <= 3 else registers[literal_operand - 4]
        if program[ip] == 0: registers[0] = registers[0] >> combo_operand
        if program[ip] == 1: registers[1] = registers[1] ^ literal_operand
        if program[ip] == 2: registers[1] = combo_operand % 8
        if program[ip] == 4: registers[1] = registers[1] ^ registers[2]
        if program[ip] == 5: r.append(combo_operand % 8)
        if program[ip] == 6: registers[1] = registers[0] >> combo_operand
        if program[ip] == 7: registers[2] = registers[0] >> combo_operand
        if program[ip] == 3 and registers[0] != 0:
            ip = literal_operand
            continue
        ip += 2
    return r


def sol1(ci):
    _, program = read(ci)
    lsolv = lambda i: solv([i, 0, 0], program)

    target_len = len(program)
    start = dichotomy(
        *(0, 10000000000000000000),
        lambda li: len(lsolv(li)) >= target_len,
        lambda li: (len(lsolv(li)) == len(program) and len(lsolv(li-1)) == len(program)-1),
    )
    for off in range(1, len(program) - 1):
        for i in range(start, start << 8, 1 << max((target_len - off - 2) * 3, 0)):
            if lsolv(i)[-off] == program[-off]:
                start = i
                break
    # So cheesy but who cares
    start -= 10000
    for i in range(start, start << 8):
        if i % 10000 == 0:  print("   ", i, lsolv(i), program)
        if lsolv(i) == program: return i  # Could do better by traversing a tree from the lowest output char I guess


def dichotomy(start, stop, condition_move_max, condition_win):
    while True:
        li = (start + stop) // 2
        if condition_move_max(li): stop = li
        else: start = li
        if condition_win(li): return li


ti = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""[1:-1]


assert(sol0(ti)) == "4,6,3,5,6,3,5,2,1,0"


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
