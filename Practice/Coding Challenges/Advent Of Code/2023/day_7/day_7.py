import functools
from functools import cmp_to_key


def read_lines(filename):
    with open(file=filename) as file:
        for line in file.read().splitlines():
            yield line


def read_input(file):
    hands = []
    for line in read_lines(file):
        hand = Hand()
        hand.cards = line.split(" ")[0]
        hand.bid = int(line.split(" ")[1])
        hands.append(hand)
    return hands


possible_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    cards = []
    bid = 0
    count = dict()
    type = 0

    def type_of_hand(hand):
        for card in hand.cards:
            if card in hand.count.keys():
                hand.count[card] += 1
            else:
                hand.count[card] = 1

        if 5 in hand.count.values():
            return "7"
        elif 4 in hand.count.values():
            return "6"
        elif 3 in hand.count.values() and 2 in hand.count.values():
            return "5"
        elif 3 in hand.count.values():
            return "4"
        elif list(hand.count.values()).count(2) > 1:
            return "3"
        elif 2 in hand.count.values():
            return "2"
        else:
            return "1"


def strength(card):
    return 13 - possible_cards.index(card)


def card_strength_sort(card1, card2):
    card1_strength = strength(card1)
    card2_strength = strength(card2)
    return (card1_strength > card2_strength) - (card1_strength < card2_strength)


def hand_strength_sort(hand1: Hand, hand2: Hand) -> int:
    hand1.type_of_hand()
    hand2.type_of_hand()

    if hand1.t != hand2_type:
        return (hand1_type > hand2_type) - (hand1_type < hand2_type)

    hand1_sorted = sorted(hand1, key=functools.cmp_to_key(card_strength_sort), reverse=True)
    hand2_sorted = sorted(hand2, key=functools.cmp_to_key(card_strength_sort), reverse=True)

    index = 0
    for index in range(len(hand1)):
        if hand1_sorted[index] != hand2_sorted[index]:
            return card_strength_sort(hand1_sorted[index], hand2_sorted[index])


if __name__ == '__main__':
    hands_and_bids = read_input("day_7_test.txt")
    sorted_hands_and_bids = sorted(hands_and_bids, key=functools.cmp_to_key(hand_strength_sort), reverse=True)
    for hand in sorted_hands_and_bids:
        print(hand)
