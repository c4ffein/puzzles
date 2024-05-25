# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


from math import prod


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")
times = [int(s) for s in ls[0].split(":")[1].split()]
distances = [int(s) for s in ls[1].split(":")[1].split()]


sol = lambda times, distances: prod(sum(1 for i in range(t) if (t - i) * i > d) for t, d in zip(times, distances))


print(sol(times, distances))
print(sol([int("".join(str(t) for t in times))], [int("".join(str(d) for d in distances))]))
