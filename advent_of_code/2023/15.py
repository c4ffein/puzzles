with open("input.txt") as f:
    inputed = f.read()


def hash(string):
    r = 0
    for c in string:
        r = (r + ord(c)) * 17 % 256
    return r


test_string = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
assert hash("HASH") == 52
assert sum(hash(e) for e in test_string.split(",")) == 1320


print(sum(hash(e) for e in inputed.split("\n")[0].split(",")))


def gen_boxes(instructions):
    ds = {i: {} for i in range(256)}
    for instruction in instructions:
        if "=" in instruction:
            string, num_string = instruction.split("=")
            h = hash(string)
            num = int(num_string)
            ds[h][string] = num
        elif "-" in instruction:
            string = instruction[:-1]
            h = hash(string)
            try:
                del ds[h][string]
            except KeyError:
                pass
        else:
            raise Exception("BAD FAIL")
    return ds


def grade(stuff):
    r = 0
    for box_k, box_v in stuff.items():
        for lens_i, lens_v in enumerate(box_v.values()):
            r += (box_k + 1) * (lens_i + 1) * lens_v
    return r


test_ds = {0: {'rn': 1, 'cm': 2}, 3: {'ot': 7, 'ab': 5, 'pc': 6}}
assert {k: v for k, v in gen_boxes(test_string.split(",")).items() if len(v) != 0} == test_ds
assert grade(test_ds) == 145


print(grade(gen_boxes(inputed.split("\n")[0].split(","))))
