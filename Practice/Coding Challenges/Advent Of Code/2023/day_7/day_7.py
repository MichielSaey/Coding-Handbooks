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

        for card in line.split(" ")[0]:
            hand.cards.append(Card(card))

        hand.bid = int(line.split(" ")[1])
        hands.append(hand)
    return hands


possible_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Card:
    def __init__(self, value):
        self.value = value
        self.amount = 0


class Hand:
    def __init__(self):
        self.cards: list[Card] = []
        self.sorted_cards = []
        self.bid = 0
        self.type = 0

    def type_of_hand(hand):
        card_count = dict()

        for card in hand.cards:
            if card.value in card_count.keys():
                card_count[card.value] += 1
            else:
                card_count[card.value] = 1

        for card in hand.cards:
            card.amount = card_count[card.value]

        if 5 in card_count.values():
            hand.type = 7
        elif 4 in card_count.values():
            hand.type = 6
        elif 3 in card_count.values() and 2 in card_count.values():
            hand.type = 5
        elif 3 in card_count.values():
            hand.type = 4
        elif list(card_count.values()).count(2) > 1:
            hand.type = 3
        elif 2 in card_count.values():
            hand.type = 2
        else:
            hand.type = 1

    def sort(self):
        self.sorted_cards = sorted(self.cards, key=functools.cmp_to_key(card_strength_sort), reverse=True)

    def to_string(self):
        cards = ""
        for card in self.cards:
            cards += card.value
        return f"Hand: {cards}, Bid: {self.bid}"


def strength(card):
    return 13 - possible_cards.index(card)


def card_strength_sort(card1: Card, card2: Card):
    card1_strength = strength(card1.value)
    card2_strength = strength(card2.value)
    if card1.amount != card2.amount:
        return (card1.amount > card2.amount) - (card1.amount < card2.amount)
    return (card1_strength > card2_strength) - (card1_strength < card2_strength)


def hand_strength_sort(hand1: Hand, hand2: Hand) -> int:
    hand1.type_of_hand()
    hand2.type_of_hand()

    if hand1.type != hand2.type:
        return (hand1.type > hand2.type) - (hand1.type < hand2.type)

    hand1.sort()
    hand2.sort()

    index = 0
    for index in range(len(hand1.cards)):
        if hand1.cards[index].value != hand2.cards[index].value:
            if hand1.cards[index].amount != hand2.cards[index].amount:
                return (hand1.cards[index].amount > hand2.cards[index].amount) - (hand1.cards[index].amount < hand2.cards[index].amount)
            return card_strength_sort(hand1.cards[index], hand2.cards[index])


if __name__ == '__main__':
    hands_and_bids = read_input("day_7.txt")
    sorted_hands_and_bids = sorted(hands_and_bids, key=functools.cmp_to_key(hand_strength_sort))
    total_winnings = 0
    for index, hand in enumerate(sorted_hands_and_bids, start=1):
        winnings = (index) * hand.bid
        total_winnings += winnings
        print(index, f"Cards: {hand.to_string()}", f"Bid: {hand.bid}", f"Winnings: {winnings}")

    print(total_winnings)
