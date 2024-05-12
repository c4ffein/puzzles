from functools import reduce
import operator


def handle_throw(dices):
    r = [0, 0, 0]
    for d in dices:
        n, color = d.split(" ")
        r[{"red": 0, "green": 1, "blue": 2}[color]] += int(n)
    return r


def parse_line(l):
    g, ts = l.split(": ")
    gn = g.split(" ")[1]
    tss = [handle_throw(t.split(", ")) for t in ts.split("; ")]
    return gn, tss


def valid_throws(throws, limits):
    return all(dices[i] <= limits[i] for dices in throws for i in range(3))


def possible_dices(throws):
    return [max(dc) for dc in zip(*throws)]


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]
print(sum(int(k) for k, v in (parse_line(l) for l in ls) if valid_throws(v, [12, 13, 14])))
print(sum(reduce(operator.mul, possible_dices(v), 1) for k, v in (parse_line(l) for l in ls)))
