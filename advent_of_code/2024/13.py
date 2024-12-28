# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf

def sol0(ci):
    ci = load_i(ci)
    return sum(solv1(*l) for l in ci)


def sol1(ci):
    ci = [(xa, pa, xb, yb, xp + 10000000000000, yp + 10000000000000) for (xa, pa, xb, yb, xp, yp) in load_i(ci)]
    return sum(solv1(*l) for l in ci)


def load_i(i):
    return [
        [
            int(l0.split(", ")[0][12:]),
            int(l0.split(", ")[1][2:]),
            int(l1.split(", ")[0][12:]),
            int(l1.split(", ")[1][2:]),
            int(l2.split(", ")[0][9:]),
            int(l2.split(", ")[1][2:]),
        ]
        for l0, l1, l2 in [b.split("\n") for b in i.split("\n\n")]
    ]


def solv0(xa, ya, xb, yb, xp, yp):
    if xa * yb == xb * ya:
        return min(xp // xa * 3, xp // xb)
    m = inf
    for pa in range(101):
        for pb in range(101):
            if pa * xa + pb * xb == xp and pa * ya + pb * yb == yp and pa * 3 + pb < m:
                m = pa * 3 + pb
    return m if m is not inf else 0

def solv1(xa, ya, xb, yb, xp, yp):
    if xa * yb == xb * ya:  # Despite that case there should be one and only one way to reach the point
        return min(xp // xa * 3, xp // xb)
    mul_a, mul_b = 3, 1
    if ya * xb > yb * xa:  # Ensures that the bigger the button b pressed ratio, the higher the y result
        xa, ya, xb, yb, mul_a, mul_b = xb, yb, xa, ya, mul_b, mul_a
    lpa = 0
    hpa = xp // xa + 1
    while lpa <= hpa:
        mpa = int((lpa + hpa) // 2)
        mxa = mpa * xa
        mxb = xp - mxa
        mpb = mxb / xb if mxb % xb != 0 else mxb // xb  # could be float, check on real validation...
        mya = mpa * ya
        myb = mpb * yb  # could be float too then, danger maybe, but just going for the star
        # print(
        #     f"A: ({xa}, {xb})   B: ({xb, yb})   T: ({xp}, {yp})   "
        #     f"[{lpa}, {hpa}]  {mxa}  {mxb}  h[A:{mya}, B:{myb}]={mya+myb}"
        # )
        if isinstance(mpb, int) and mya + myb == yp:
            return mpa * mul_a + mpb * mul_b
        if lpa == hpa:
            return 0  # If was possible, would have returned better value earlier
        if mya + myb > yp:  # Too much b presses, too little a presses
            lpa = mpa if lpa != mpa else lpa + 1
        else:   # Too much a presses, too little b presses
            hpa = mpa if hpa != mpa else hpa - 1
    return 0  # overdrove so impossible


ti = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""[1:-1]


assert(sol0(ti)) == 480


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    ri = []
print(sol0(ri))
print(sol1(ri))
