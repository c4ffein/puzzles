# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from sys import setrecursionlimit

setrecursionlimit(1000000000)

dirs = {
    "^": lambda x, y: (x, y-1),
    ">": lambda x, y: (x+1, y),
    "v": lambda x, y: (x, y+1),
    "<": lambda x, y: (x-1, y),
}
dirs_list = [k for k in dirs]
left  = lambda d: dirs_list[(dirs_list.index(d) - 1) % 4]
right = lambda d: dirs_list[(dirs_list.index(d) + 1) % 4]


def odirs(d, x, y):
    if d == 0: return (x, y-1)
    if d == 1: return (x+1, y)
    if d == 2: return (x, y+1)
    if d == 3: return (x-1, y)


def sol0(ci):
    player = [(x, y) for y in range(len(ci)) for x in range(len(ci[0])) if ci[y][x] == "S"][0]
    current_dir = ">"
    end = [(x, y) for y in range(len(ci)) for x in range(len(ci[0])) if ci[y][x] == "E"][0]
    g = [[c == "#" for c in l] for l in ci]
    sg = [[{"^": inf, ">": inf, "v": inf, "<": inf} for c in l] for l in ci]
    return solv0(g, sg, player, current_dir, end, 0)


def solv0(g, sg, player, current_dir, end, score):
    if player == end:
        return score
    if g[player[1]][player[0]]:
        return inf
    if score >= sg[player[1]][player[0]][current_dir]:  # >= because we don't care about duplicates I guess
        return inf
    sg[player[1]][player[0]][current_dir] = score
    return min(
        solv0(g, sg, dirs[current_dir](*player), current_dir, end, score + 1),
        solv0(g, sg, player, left(current_dir), end, score + 1000),
        solv0(g, sg, player, right(current_dir), end, score + 1000),
    )


def sol1(ci):
    limit_max = sol0(ci)
    player = [(x, y) for y in range(len(ci)) for x in range(len(ci[0])) if ci[y][x] == "S"][0]
    current_dir = 1
    end = [(x, y) for y in range(len(ci)) for x in range(len(ci[0])) if ci[y][x] == "E"][0]
    g = [[c == "#" for c in l] for l in ci]
    sg = [[([inf] * 4) for c in l] for l in ci]
    r = solv1(g, sg, player, current_dir, end, 0, limit_max)
    return len(r)


def solv1(g, sg, player, current_dir, end, score, limit_max):
    if score > limit_max:
        return set()
    if player == end:
        return {player}
    if g[player[1]][player[0]]:
        return set()
    if score > sg[player[1]][player[0]][current_dir]:  # > because for that part we care about dupplicates
        return set()
    sg[player[1]][player[0]][current_dir] = score
    x, y = player
    r = (
        solv1(
            g,
            sg,
            [(x, y-1), (x+1, y), (x, y+1), (x-1, y)][current_dir],
            current_dir,
            end,
            score + 1,
            limit_max,
        )
        | solv1(g, sg, player, (current_dir-1) % 4, end, score + 1000, limit_max)
        | solv1(g, sg, player, (current_dir+1) % 4, end, score + 1000, limit_max)
    )
    return (r | {player}) if r else r


ti = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""[1:-1].split("\n")


assert(sol0(ti)) == 7036


try:
    with open("input.txt") as f:
        ri = f.read().split("\n")[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
