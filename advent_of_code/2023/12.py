from functools import lru_cache


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]


lines = [[line, [int(n) for n in numbers.split(",")]] for l in ls for line, numbers in [l.split(" ")]]


@lru_cache
def solve(line, numbers):
    if not line:
        return 1 if len(numbers) == 0 else 0
    if len(numbers) == 0:
        return 0 if "#" in line else 1
    if line[0] == "#":
        if len(numbers) == 0:
            return 0
        if len(line) < numbers[0]:
            return 0
        if "." in line[:numbers[0]]:
            return 0
        if len(line) == numbers[0]:
            return 1 if len(numbers) == 1 else 0
        if line[numbers[0]] == "#":
            return 0
        return solve(line[numbers[0] + 1:], numbers[1:])
    if line[0] == ".":
        return solve(line[1:], numbers)
    if line[0] == "?":
        return solve("#" + line[1:], numbers) + solve("." + line[1:], numbers)


print(sum(solve(line, tuple(numbers)) for line, numbers in lines))
print(sum(solve((f"{line}?" * 5)[:-1], tuple(numbers * 5)) for line, numbers in lines))
