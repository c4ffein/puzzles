words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def first_number(s, words):
    for i in range(len(s)):
        if s[i] in "0123456789":
            return s[i]
        for n, w in words.items():
            if s[i:].startswith(w):
                return str(n)
    raise Exception(f"Nothing found in {s}")


def last_number(s, words):
    return first_number("".join(reversed(s)), words={k: "".join(reversed(v)) for k, v in words.items()})


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]
print(sum(int(first_number(l, {}   ) + last_number(l, {}   )) for l in ls))
print(sum(int(first_number(l, words) + last_number(l, words)) for l in ls))
