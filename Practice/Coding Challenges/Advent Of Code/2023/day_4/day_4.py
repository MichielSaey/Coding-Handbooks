def read_lines(filename):
    with open(file=filename) as file:
        for line in file.read().splitlines():
            yield line


class Card:
    cards: [] = list()

    def __init__(self, id: int, picked_numbers: [], winning_numbers: []):
        self.id: int = int(id)
        self.picked_numbers: list = picked_numbers
        self.winning_numbers: list = winning_numbers
        self.copies = 1

    def to_string(self):
        return f"Card {self.id}: instanses = {self.copies}"

    @classmethod
    def get_cards(cls):
        return cls.cards

    @classmethod
    def from_line(cls, line):
        line_prefix = line.split(":")[0]
        line_prefix = filter(lambda element: element != "" , line_prefix.split(" "))
        id = list(line_prefix)[1]
        numbers = line.split(":")[1]
        picked_numbers = numbers.split("|")[0].strip().split(" ")
        picked_numbers = list(filter(lambda element: element != "", picked_numbers))
        winning_numbers = numbers.split("|")[1].strip().split(" ")
        winning_numbers = list(filter(lambda element: element != "", winning_numbers))
        card = cls(id, picked_numbers, winning_numbers)
        cls.cards.append(card)
        return card

    @classmethod
    def copy_following_cards(cls, start_card, cards_to_copy):
        print(f"Copy from {start_card} which has {Card.cards[start_card - 1].copies}")
        index = start_card
        while index < start_card + cards_to_copy:
            cls.cards[index].copy(start_card)
            index += 1

    def calculate_points(self):
        points = 0
        all_numbers = self.picked_numbers + self.winning_numbers
        for winning_number in self.winning_numbers:
            count = all_numbers.count(winning_number)
            if count >= 2:
                if points == 0:
                    points += 1
                else:
                    points *= 2

        return points

    def calculate_copies(self):
        points = 0
        all_numbers = self.picked_numbers + self.winning_numbers
        for winning_number in self.winning_numbers:
            count = all_numbers.count(winning_number)
            if count >= 2:
                points += 1

        Card.copy_following_cards(self.id, points)
        return self.copies

    def copy(self, copy_from):
        add_to_copy = Card.cards[copy_from - 1].copies
        self.copies = self.copies + add_to_copy
        print(f"To Card {self.id} which now has {self.copies} instances")


if __name__ == '__main__':
    for line in read_lines("day_4.txt"):
        Card.from_line(line)

    copy_count = 0
    for card in Card.get_cards():
        copy_count += card.calculate_copies()
        print(card.to_string())

    print(copy_count)

