# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

def sol0(ci):
    return checksum(rework(expand(ci)))


def sol1(ci):
    return checksum(new_rework(expand(ci)))


def expand(ci):
    r = []
    for i, c in enumerate(ci):
        r += ([i // 2] if (i%2) == 0 else [None]) * int(c)
    return r


def rework(ei):
    i = 0
    while i < len(ei):
        while ei[i] is None:
            ei[i] = ei[-1]
            ei = ei[:-1]
        i += 1
    return ei


def checksum(ei):
    return sum(i * (v if v is not None else 0) for i, v in enumerate(ei))


def new_rework(ei):
    i = len(ei) - 1
    while i > 0:
        v = ei[i]
        ci = i
        length_of_block = 0
        while ei[ci] == v:
            length_of_block += 1
            ci -= 1
        j = 0
        while j < i:
            nn = 0
            while ei[j + nn] is None:
                nn += 1
            if length_of_block <= nn:
                for replacer_index in range(j, j+length_of_block):
                    ei[replacer_index] = v
                for replacer_index in range(i-length_of_block+1, i+1):
                    ei[replacer_index] = None
                break
            j += 1
        i -= length_of_block
    return ei

ti = "2333133121414131402"

assert expand(ti) == [0, 0, None, None, None, 1, 1, 1, None, None, None, 2, None, None, None, 3, 3, 3, None, 4, 4, None, 5, 5, 5, 5, None, 6, 6, 6, 6, None, 7, 7, 7, None, 8, 8, 8, 8, 9, 9]
assert "".join(str(c) for c in rework(expand(ti))) == "0099811188827773336446555566"
assert checksum(rework(expand(ti))) == 1928
assert sol0(ti) == 1928
assert "".join(str(c) if c is not None else "X" for c in new_rework(expand(ti))) == "00992111777X44X333XXXX5555X6666XXXXX8888XX"
assert sol1(ti) == 2858


with open("input.txt") as f:
    ri = f.read()[:-1]

print(sol0(ri))
print(sol1(ri))
