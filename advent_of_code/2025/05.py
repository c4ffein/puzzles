#!/usr/bin/env python3

"""
This was made entirely by Claude (from Anthropic). No nudging whatsoever.
"""


def parse_input(filename):
    with open(filename) as f:
        content = f.read().strip()

    # Split into ranges section and ingredients section
    parts = content.split('\n\n')
    range_lines = parts[0].strip().split('\n')
    ingredient_lines = parts[1].strip().split('\n')

    # Parse ranges
    ranges = []
    for line in range_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    # Parse ingredient IDs
    ingredients = [int(line) for line in ingredient_lines]

    return ranges, ingredients


def part1(ranges, ingredients):
    """Count how many ingredient IDs fall within at least one range."""
    fresh_count = 0
    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                fresh_count += 1
                break
    return fresh_count


def part2(ranges):
    """Count total unique IDs covered by all ranges (merge overlapping ranges)."""
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)

    # Merge overlapping ranges
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # Overlapping or adjacent
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    # Count total IDs in merged ranges
    total = sum(end - start + 1 for start, end in merged)
    return total


if __name__ == "__main__":
    ranges, ingredients = parse_input("input.md")

    print(f"Part 1: {part1(ranges, ingredients)}")
    print(f"Part 2: {part2(ranges)}")
