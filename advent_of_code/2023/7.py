with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]
hands = {k: int(v) for e in ls for (k, v) in [e.split()]}


def get_score(hand, real_hand=None, replace=False):
    card_power = (
        [*reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])]
        if replace == False
        else [*reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])]
    )
    if real_hand is None:
        real_hand = hand
    if replace and "J" in hand:
        i = hand.index("J")
        return max(
            get_score(hand[:i] + r + hand[i+1:], real_hand=real_hand, replace=True)
            for r in set(hand+"A") - set("J")
        )
    card_count = {k: 0 for k in card_power}
    for card in hand:
        card_count[card] += 1
    # Five of a kind, where all five cards have the same label: AAAAA
    if 5 in card_count.values():
        return 7, [card_power.index(c) for c in real_hand]
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    if 4 in card_count.values():
        return 6, [card_power.index(c) for c in real_hand]
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    if 3 in card_count.values() and 2 in card_count.values():
        return 5, [card_power.index(c) for c in real_hand]
    # Three of a kind, where three cards have the same label,
    # and the remaining two cards are each different from any other card in the hand: TTT98
    if 3 in card_count.values():
        return 4, [card_power.index(c) for c in real_hand]
    # Two pair, where two cards share one label, two other cards share a second label,
    # and the remaining card has a third label: 23432
    if len([v for v in card_count.values() if v == 2]) == 2:
        return 3, [card_power.index(c) for c in real_hand]
    # One pair, where two cards share one label,
    # and the other three cards have a different label from the pair and each other: A23A4
    if 2 in card_count.values():
        return 2, [card_power.index(c) for c in real_hand]
    # High card, where all cards' labels are distinct: 23456
    return 1, [card_power.index(c) for c in real_hand]


def solve(replace=False):
    hands_list = [*sorted((h for h in hands), key = lambda h: get_score(h, replace=replace))]
    return sum(bid * (hands_list.index(hand) + 1) for hand, bid in hands.items())


print(solve())
print(solve(replace=True))
