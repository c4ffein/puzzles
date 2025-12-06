#!/usr/bin/env python3

"""
This was made entirely by Claude (from Anthropic). No nudging whatsoever.
"""


# 8 directions: up, down, left, right, and 4 diagonals
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]


def read_grid(input_file):
    with open(input_file) as f:
        return [list(line.rstrip('\n')) for line in f]


def find_accessible(grid):
    """Find all rolls with fewer than 4 adjacent rolls."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent_rolls = sum(
                    1 for dr, dc in DIRECTIONS
                    if 0 <= r + dr < rows and 0 <= c + dc < cols
                    and grid[r + dr][c + dc] == '@'
                )
                if adjacent_rolls < 4:
                    accessible.append((r, c))

    return accessible


def part1(input_file):
    grid = read_grid(input_file)
    return len(find_accessible(grid))


def part2(input_file):
    grid = read_grid(input_file)
    total_removed = 0

    while True:
        accessible = find_accessible(grid)
        if not accessible:
            break
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'
        total_removed += len(accessible)

    return total_removed


if __name__ == "__main__":
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")
