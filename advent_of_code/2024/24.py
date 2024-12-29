# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from pprint import pprint as pp
from enum import Enum


Ops = Enum("Ops", ["AND", "OR", "XOR"])
compute_op = lambda op, a, b: (a & b) if op == Ops.AND.value else a | b if op == Ops.OR.value else a ^ b


def load(ci):
    starters_s, operations_s = ci.split("\n\n")
    starters = {k: int(v) for k, v in [l.split(": ") for l in starters_s.split("\n")]}
    operations = [[Ops[op].value, a, b, r] for a, op, b, _, r in [l.split(" ") for l in operations_s.split("\n")]]
    return starters, operations


def sol0(ci):
    values, ops = load(ci)
    key_to_operations = {k: [op for op in ops if k in op[1:3]] for k in {op[i] for op in ops for i in [1, 2]}}
    keys_to_treat = set(values)
    while keys_to_treat:
        value = keys_to_treat.pop()
        current_list = key_to_operations.get(value, None)
        if current_list is None: continue
        for op, a, b, r in current_list:
            if a in values and b in values and r not in values:
                values[r] = compute_op(op, values[a], values[b])
                keys_to_treat.add(r)
        del key_to_operations[value]
    return int(
        "".join([str(v) for _, v in sorted((-int(k[1:]), v) for k, v in values.items() if k.startswith("z"))]), 2
    )


class Node:
    def __init__(self, op_name, operand, a, b):
        self.op_name, self.operand, self.a, self.b = op_name, operand, a, b

    def __eq__(self, node):
        if isinstance(node, str): return False
        return (
            self.operand == node.operand
            and ((self.a == node.a and self.b == node.b) or (self.a == node.b and self.b == node.a))
        )

    def find_discrepancies(self, node):  # Always find the highest, may be a problem if you have 2 switches in the same,
        gn = lambda n: n if isinstance(n, str) else n.op_name # shouldn't be a problem due to the wires architecture tho
        if isinstance(node, str): return self.op_name
        if self == node: return None
        if self.operand != node.operand: return self.op_name
        if any((self.a, self.b) == (a, b) for a, b in ((node.a, node.b), (node.b, node.a))): return
        if self.a == node.a: return self.b.find_discrepancies(node.b) if isinstance(self.b, Node) else gn(self.b)
        if self.b == node.b: return self.a.find_discrepancies(node.a) if isinstance(self.a, Node) else gn(self.a)
        if self.a == node.b: return self.b.find_discrepancies(node.a) if isinstance(self.b, Node) else gn(self.b)
        if self.b == node.a: return self.a.find_discrepancies(node.b) if isinstance(self.b, Node) else gn(self.b)
        return self.op_name


f_and, f_or, f_xor = [(lambda op: (lambda a, b: Node("", op.value, a, b)))(op) for op in [Ops.AND, Ops.OR, Ops.XOR]]


def sol1(ci, replacement_pairs = None):
    replacement_pairs = replacement_pairs or []
    replacements = {(b if rev else a): (a if rev else b) for a, b in replacement_pairs for rev in [True, False]}
    values, operations = load(ci)
    operations = [[*op[:3], replacements.get(op[3], op[3])] for op in operations]
    operations_by_result = {op[3]: op for op in operations}
    ends = sorted(op[3] for op in operations if op[3][0] == "z")

    def make_node_from_name(name, r=[], traversed=[]):  # Bad but won't mutate those optionals
        name = name if name not in r else [o for o in r if o != name][0]
        if traversed and name in traversed: return "ONO"  # cheese to keep consistent with existing code
        op = operations_by_result.get(name, None)
        if op is None: return name
        return Node(op[3], op[0], *(make_node_from_name(op[ci], r, [*traversed, name]) for ci in [1, 2]))

    assert make_node_from_name(ends[0]) == f_xor("x00", "y00")
    assert make_node_from_name(ends[1]) == f_xor(f_xor("x01", "y01"), f_and("x00", "y00"))
    carry = f_and("x00", "y00")
    nx, ny = (lambda i: f"x{str(i).zfill(2)}"), (lambda i: f"y{str(i).zfill(2)}")
    make_carry = lambda prev, cid: Node("", Ops.OR.value, f_and(nx(i-1), ny(i-1)), f_and(f_xor(nx(i-1), ny(i-1)), prev))
    for i in range(2, len(ends)):
        carry = make_carry(carry, i)
        parsed_node = make_node_from_name(ends[i])
        computed_node = f_xor(f_xor(nx(i), ny(i)), carry) if i < len(ends) - 1 else carry
        disc = parsed_node.find_discrepancies(computed_node)
        if not disc:  continue
        if disc in replacements: raise Exception("Change already handled")
        for op in [o for o in operations_by_result if o not in [*replacements, disc]]:
            if make_node_from_name(ends[i], r=[disc, op]) == computed_node:
                return sol1(ci, [*replacement_pairs, (disc, op)])
        raise Exception("No dual found")
    return ",".join(sorted(v for a, b in replacement_pairs for v in [a, b]))


ti = """
x00: 1\nx01: 0\nx02: 1\nx03: 1\nx04: 0\ny00: 1\ny01: 1\ny02: 1\ny03: 1\ny04: 1

ntg XOR fgs -> mjb\ny02 OR x01 -> tnw_\nkwq OR kpj -> z05_\nx00 OR x03 -> fst_\ntgd XOR rvg -> z01\nvdt OR tnw -> bfw_
bfw AND frj -> z10\nffh OR nrd -> bqk_\ny00 AND y03 -> djm\ny03 OR y00 -> psh_\nbqk OR frj -> z08_\ntnw OR fst -> frj_
gnj AND tgd -> z11\nbfw XOR mjb -> z00\nx03 OR x00 -> vdt_\ngnj AND wpb -> z02\nx04 AND y00 -> kjc\ndjm OR pbm -> qhw_
nrd AND vdt -> hwm\nkjc AND fst -> rvg\ny04 OR y02 -> fgs_\ny01 AND x02 -> pbm\nntg OR kjc -> kwq_\npsh XOR fgs -> tgd
qhw XOR tgd -> z09\npbm OR djm -> kpj_\nx03 XOR y03 -> ffh\nx00 XOR y04 -> ntg\nbfw OR bqk -> z06_\nnrd XOR fgs -> wpb
frj XOR qhw -> z04\nbqk OR frj -> z07_\ny03 OR x01 -> nrd_\nhwm AND bqk -> z03\ntgd XOR rvg -> z12\ntnw OR pbm -> gnj_
"""[1:-1].replace("_", "")


assert(sol0(ti)) == 2024


try:
    with open("input.txt") as f:
        ri = f.read()[:-1]
except FileNotFoundError:
    print("Wainting for input.")
    exit(-4)
print(sol0(ri))
print(sol1(ri))
