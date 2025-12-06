#!/usr/bin/env python3

"""
This was made entirely by Claude (from Anthropic). No nudging whatsoever.
"""


def generate_invalid_in_range(start, end):
    """Generate all invalid IDs within a given range (Part 1: exactly twice)."""
    invalid_ids = []

    min_digits = len(str(start))
    max_digits = len(str(end))

    for total_digits in range(min_digits, max_digits + 1):
        if total_digits % 2 != 0:
            continue  # Invalid IDs must have even length for exactly 2 repetitions

        half_digits = total_digits // 2

        # X ranges from 10^(half_digits-1) to 10^half_digits - 1
        # For half_digits=1, X ranges from 1 to 9 (no leading zeros)
        if half_digits == 1:
            x_start = 1
        else:
            x_start = 10 ** (half_digits - 1)
        x_end = 10 ** half_digits - 1

        for x in range(x_start, x_end + 1):
            invalid_id = int(str(x) + str(x))
            if start <= invalid_id <= end:
                invalid_ids.append(invalid_id)

    return invalid_ids


def generate_invalid_in_range_v2(start, end):
    """Generate all invalid IDs within a given range (Part 2: at least twice)."""
    invalid_ids = set()  # Use set to avoid duplicates (e.g., 1111 = "1"*4 or "11"*2)

    min_digits = len(str(start))
    max_digits = len(str(end))

    for total_digits in range(min_digits, max_digits + 1):
        # Try all possible pattern lengths that divide total_digits
        for pattern_len in range(1, total_digits // 2 + 1):
            if total_digits % pattern_len != 0:
                continue

            repetitions = total_digits // pattern_len
            if repetitions < 2:
                continue

            # Pattern ranges from 10^(pattern_len-1) to 10^pattern_len - 1
            # For pattern_len=1, ranges from 1 to 9 (no leading zeros)
            if pattern_len == 1:
                p_start = 1
            else:
                p_start = 10 ** (pattern_len - 1)
            p_end = 10 ** pattern_len - 1

            for p in range(p_start, p_end + 1):
                invalid_id = int(str(p) * repetitions)
                if start <= invalid_id <= end:
                    invalid_ids.add(invalid_id)

    return list(invalid_ids)


def solve(input_str):
    """Parse input and sum all invalid IDs across all ranges (Part 1)."""
    ranges = input_str.strip().split(',')
    total = 0

    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split('-'))
        invalid_ids = generate_invalid_in_range(start, end)
        total += sum(invalid_ids)

    return total


def solve_v2(input_str):
    """Parse input and sum all invalid IDs across all ranges (Part 2)."""
    ranges = input_str.strip().split(',')
    total = 0

    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split('-'))
        invalid_ids = generate_invalid_in_range_v2(start, end)
        total += sum(invalid_ids)

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read()

    result1 = solve(input_data)
    print(f"Part 1 - Sum of all invalid IDs: {result1}")

    result2 = solve_v2(input_data)
    print(f"Part 2 - Sum of all invalid IDs: {result2}")
