# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


from itertools import count
from heapq import heappush, heappop


with open("input.txt") as f:
    i = f.read()
input_grid = i.split("\n")[:-1]


# From Python documentation : https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
# Modified as add_node needs to handle the search for a minimum instead
class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<Removed>'
        self.counter = count()

    def add_node(self, node, score):
        existing_entry = self.entry_finder.get(node, None)
        if existing_entry is not None:
            if existing_entry[0] <= score:
                return
            entry = self.entry_finder.pop(node)
            entry[-1] = self.REMOVED
        count = next(self.counter)
        entry = [score, count, node]
        self.entry_finder[node] = entry
        heappush(self.pq, entry)

    def pop_node(self):
        while self.pq:
            score, count, node = heappop(self.pq)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return node, score
        return None, 0


def get_all_reachables(x, y, min_move, max_move):
    return [
        (*f(i), [f(j) for j in range(1, i + 1)])
        for i in range(min_move, max_move)
        for f in [lambda d: (x, y - d), lambda d: (x, y + d), lambda d: (x - d, y), lambda d: (x + d, y)]
    ]


def make_nodes(grid, min_move, max_move):
    igrid = [[int(c) for c in l] for l in grid]
    nodes_with_dir = {}
    passing_scores = {}
    for y, l in enumerate(igrid):
        for x, c in enumerate(l):
            all_reachables = [
                (rx, ry, walked)
                for (rx, ry, walked) in get_all_reachables(x, y, min_move, max_move)
                if (0 <= rx < len(grid[0]) and 0 <= ry < len(grid))
            ]
            for rx, ry, passed_through in all_reachables:
                passing_scores[(x, y, rx, ry)] = sum(igrid[sy][sx] for (sx, sy) in passed_through)
            nodes_with_dir[(x, y, False)] = [(nx, ny) for (nx, ny, _) in all_reachables if nx == x]
            nodes_with_dir[(x, y, True)] = [(nx, ny) for (nx, ny, _) in all_reachables if ny == y]
    return nodes_with_dir, passing_scores


def solve(grid, min_move=1, max_move=4):
    nodes_with_dir, passing_scores = make_nodes(grid, min_move, max_move)
    done = {}
    tosee = PriorityQueue()
    tosee.add_node((0, 0, False), 0)
    tosee.add_node((0, 0, True), 0)
    while True:
        current, current_score = tosee.pop_node()
        if current is None:
            break
        done[current] = current_score
        for next_reach in nodes_with_dir[current]:
            next_node = (*next_reach, not current[2])
            if next_node in done:
                continue
            tosee.add_node(next_node, current_score + passing_scores[current[:2] + next_node[:2]])
    return min(done[node] for node in [(len(grid[0]) - 1, len(grid) - 1, i) for i in [True, False]])
        

test_grid = (
    "2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n"
    "4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n"
    "4322674655533"
).split("\n")
assert solve(test_grid) == 102
print("TESTS PASSED")
print(solve(input_grid))
print(solve(input_grid, min_move=4, max_move=11))
