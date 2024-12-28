# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality

from math import inf
from pprint import pprint as pp
from enum import Enum


Ops = Enum("Ops", ["AND", "OR", "XOR"])
op_name_to_value = {e.name: e.value for e in Ops}
op_value_to_name = {e.value: e.name for e in Ops}
ops_dict = {
    Ops.AND.value: lambda a, b: (a & b),
    Ops.OR.value: lambda a, b: (a | b),
    Ops.XOR.value: lambda a, b: (a ^ b),
}


def load(ci):
    starters_s, operations_s = ci.split("\n\n")
    starters = {k: int(v) for k, v in [l.split(": ") for l in starters_s.split("\n")]}
    key_to_operations = {}
    operations = []
    for l in operations_s.split("\n"):
        a, op, b, _, r = l.split(" ")
        operations.append([op_name_to_value[op], a, b, r])
        if a not in key_to_operations: key_to_operations[a] = []
        if b not in key_to_operations: key_to_operations[b] = []
        key_to_operations[a].append(operations[-1])
        key_to_operations[b].append(operations[-1])
    return starters, operations, key_to_operations


def sol0(ci):
    values, operations, key_to_operations = load(ci)
    keys_to_treat = set(values)
    while keys_to_treat:
        value = keys_to_treat.pop()
        current_list = key_to_operations.get(value, None)
        if current_list is None: continue
        for op, a, b, r in current_list:
            if a in values and b in values and r not in values:
                values[r] = ops_dict[op](values[a], values[b])
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

    def find_discrepancies(self, node):
        gn = lambda n: n if isinstance(n, str) else n.op_name
        if isinstance(node, str): return [self.op_name]
        if self == node: return []
        if self.operand != node.operand:
            return [self.op_name]
        if self.a == node.a:
            if self.b == node.b: return []
            return self.b.find_discrepancies(node.b) if isinstance(self.b, Node) else [gn(self.b)]
        if self.b == node.b: return self.a.find_discrepancies(node.a) if isinstance(self.a, Node) else [gn(self.a)]
        if self.a == node.b:
            if self.b == node.a: return []
            return self.b.find_discrepancies(node.a) if isinstance(self.b, Node) else [gn(self.b)]
        if self.b == node.a: return self.a.find_discrepancies(node.b) if isinstance(self.b, Node) else [gn(self.b)]
        return [self.op_name+node.op_name]

    def __str__(self):
        return f"{self.op_name}:=({self.a} {op_value_to_name[self.operand]} {self.b})"

make_and = lambda a, b: Node("", Ops.AND.value, a, b)
make_or  = lambda a, b: Node("", Ops.OR.value, a, b)
make_xor = lambda a, b: Node("", Ops.XOR.value, a, b)


# z00 = X00
# z01 = X01 XOR A00
# z02 = X02 XOR ( A01 OR ( X01 AND A00 ) )
# z03 = X03 XOR ( A02 OR ( X02 AND ( A01 OR ( X01 AND A00 ) ) ) )
# z04 = X04 XOR ( A03 OR ( X03 AND ( A02 OR ( X02 AND ( A01 OR ( X01 AND A00 ) ) ) ) ) )
# z05 = X05 XOR ( A04 OR ( X04 AND ( A03 OR ( X03 AND ( A02 OR ( X02 AND ( A01 OR ( X01 AND A00 ) ) ) ) ) ) )  )


def sol1(ci, replacement_pairs = None):
    replacement_pairs = replacement_pairs or []
    replacements = {
        (b if reverse else a): (a if reverse else b) for a, b in replacement_pairs for reverse in [True, False]
    }
    values, operations, key_to_operations = load(ci)
    operations = [[*op[:3], replacements.get(op[3], op[3])] for op in operations]
    operations_by_result = {op[3]: op for op in operations}
    ends = sorted(op[3] for op in operations if op[3][0] == "z")
    def make_node_from_op_name(op_name, r=None, traversed=None):
        op_name = op_name if not r or op_name not in r else [o for o in r if o != op_name][0]
        if traversed and op_name in traversed: return "ONO"  # cheese to keep consistent with existing code
        traversed = [*traversed, op_name] if traversed else [op_name]  # in case we explored a created loop
        op = operations_by_result.get(op_name, None)
        if op is None: return op_name
        return Node(op[3], op[0], *(make_node_from_op_name(op[ci], r, traversed) for ci in [1, 2]))
    assert make_node_from_op_name(ends[0]) == make_xor("x00", "y00")
    assert make_node_from_op_name(ends[1]) == make_xor(make_xor("x01", "y01"), make_and("x00", "y00"))
    carry = make_and("x00", "y00")
    make_carry = lambda prev, cid: Node("", Ops.OR.value,
        make_and(*(f"{l}{str(cid-1).zfill(2)}" for l in ["x", "y"])),
        make_and(make_xor(*(f"{l}{str(cid-1).zfill(2)}" for l in ["x", "y"])), prev),
    )
    for i in range(2, len(ends)):
        carry = make_carry(carry, i)
        parsed_node = make_node_from_op_name(ends[i])
        computed_node = (
            make_xor(make_xor(*(f"{l}{str(i).zfill(2)}" for l in ["x", "y"])), carry)
            if i < len(ends) - 1
            else carry
        )
        discs = parsed_node.find_discrepancies(computed_node)
        if len(discs) > 1: raise Exception("won't handle multiple discs detected for now")
        if len(discs) == 1:
            already_handled = [x for a, b in replacement_pairs for x in [a, b]]
            if discs[0] in already_handled: raise Exception("change already handled")
            for op in [o for o in operations_by_result if o not in [*already_handled, discs[0]]]:
                if make_node_from_op_name(ends[i], r=[discs[0], op]) == computed_node:
                    return sol1(ci, [*replacement_pairs, (discs[0], op)])
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
    ri = []
print(sol0(ri))
print(sol1(ri))
