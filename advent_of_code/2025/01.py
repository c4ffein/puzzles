#!/usr/bin/env python3

"""
This was made entirely by Claude (from Anthropic). No nudging whatsoever.
"""


import sys


def solve_part1(instructions: list[str]) -> int:
    position = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "L":
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def solve_part2(instructions: list[str]) -> int:
    position = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        # Calculate how many times we pass through 0 during this rotation
        if direction == "L":
            r = position % 100
        else:  # R
            r = (100 - position) % 100

        first_zero = r if r > 0 else 100
        if first_zero <= distance:
            zero_count += (distance - first_zero) // 100 + 1

        # Update position
        if direction == "L":
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

    return zero_count


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            instructions = [line.strip() for line in f if line.strip()]
    else:
        # Example from puzzle description
        instructions = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        print("Using example input (pass a file as argument for real input)")

    print(f"Part 1: {solve_part1(instructions)}")
    print(f"Part 2: {solve_part2(instructions)}")


if __name__ == "__main__":
    main()
