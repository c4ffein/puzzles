# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


with open("input.txt") as f:
    i = f.read()
ls = i.split("\n")[:-1]

cards = []
for l in ls:
    card_name, card_data = l.split(": ")
    winnings, played = card_data.split("|")
    winnings = [int(s) for s in winnings.split(" ") if s]
    played = [int(s) for s in played.split(" ") if s]
    cards.append([winnings, played])


def score_v1(winnings, played):
    s = sum(1 for p in played if p in winnings)
    return s if s < 2 else 2 ** (s-1)
print(sum(score_v1(winnings, played) for winnings, played in cards))


cards_instances = [1] * len(cards)
for index, ((winnings, played), multiplier) in enumerate(zip(cards, cards_instances)):
    nexts = sum(1 for p in played if p in winnings)
    for i in range(nexts):
        cards_instances[index + i + 1] += multiplier
print(sum(cards_instances))
