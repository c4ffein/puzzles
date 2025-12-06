#!/usr/bin/env python3

"""
This was made entirely by Claude (from Anthropic). No nudging whatsoever.
"""


def max_joltage_k(line, k):
    '''Select k digits from line (maintaining order) to maximize the number'''
    n = len(line)
    if k >= n:
        return line
    result = []
    start = 0
    for i in range(k):
        # For position i, we can choose from [start, n - (k - i - 1))
        # Need to leave (k - i - 1) digits after current choice
        end = n - (k - i - 1)
        # Find max digit in range [start, end)
        best_pos = start
        for j in range(start, end):
            if line[j] > line[best_pos]:
                best_pos = j
        result.append(line[best_pos])
        start = best_pos + 1
    return ''.join(result)


def solve(filename):
    part1 = 0
    part2 = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Part 1: k=2
            max_j = 0
            for i in range(len(line) - 1):
                first = int(line[i])
                second = max(int(c) for c in line[i+1:])
                max_j = max(max_j, first * 10 + second)
            part1 += max_j
            # Part 2: k=12
            part2 += int(max_joltage_k(line, 12))

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':
    solve('input.txt')
