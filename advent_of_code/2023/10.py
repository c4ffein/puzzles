from collections import namedtuple


Position = namedtuple("Position", ["x", "y"])


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]

movs = {
    "|": lambda p, c: Position(c.x, c.y + 1) if p.y < c.y else Position(c.x, c.y - 1),
    "-": lambda p, c: Position(c.x + 1, c.y) if p.x < c.x else Position(c.x - 1, c.y),
    "L": lambda p, c: Position(c.x, c.y - 1) if p.x > c.x else Position(c.x + 1, c.y),
    "J": lambda p, c: Position(c.x, c.y - 1) if p.x < c.x else Position(c.x - 1, c.y),
    "7": lambda p, c: Position(c.x, c.y + 1) if p.x < c.x else Position(c.x - 1, c.y),
    "F": lambda p, c: Position(c.x, c.y + 1) if p.x > c.x else Position(c.x + 1, c.y),
}


s_pos = next(Position(x, y) for y, l in enumerate(ls) for x, c in enumerate(l) if c == "S")
loop = set([s_pos])
prev = s_pos
# cheesing right, top and bottom bad, may not work for you
curr = Position(s_pos.x + 1, s_pos.y)
while curr not in loop:
    loop.add(curr)
    prev, curr = curr, movs[ls[curr.y][curr.x]](prev, curr)


for y, l in enumerate(ls):
    print("".join(f"\033[92m{c}\033[0m" if Position(x, y) in loop else c for x, c in enumerate(l)))


print("\nSOLUTION 1:", len(loop) // 2)


r = 0
for y, l in enumerate(ls):
    inside_loop = False
    in_tunnel_from_top = False
    in_tunnel_from_bottom = False
    for x, c in enumerate(l):
        if Position(x, y) in loop:
            if c == "F":
                in_tunnel_from_bottom = True
            if c == "L":
                in_tunnel_from_top = True
            if c == "J":
                if in_tunnel_from_bottom:
                    inside_loop = not inside_loop
                in_tunnel_from_top = in_tunnel_from_bottom = False
            if c == "7":
                if in_tunnel_from_top:
                    inside_loop = not inside_loop
                in_tunnel_from_top = in_tunnel_from_bottom = False
            if c == "|":
                inside_loop = not inside_loop
        else:
            if inside_loop:
                r += 1
print("\nSOLUTION 2:", r)
