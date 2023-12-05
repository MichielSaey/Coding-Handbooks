import re


def read_lines(filename):
    with open(file=filename) as file:
        for line in file.read().splitlines():
            yield line


class Set:
    red = 0
    green = 0
    blue = 0

    def set_red(self, red_amount):
        self.red = red_amount

    def set_green(self, green_amount):
        self.green = green_amount

    def set_blue(self, blue_amount):
        self.blue = blue_amount


class Game:
    def __init__(self, line):
        line = line.split(" ")
        self.id = re.findall('\d+', line[1])[0]
        self.sets = []
        index = 2
        set = Set()
        while index < len(line):
            amount = int(line[index])
            color = line[index + 1]

            match color


if __name__ == '__main__':
    list_of_games = []
    for line in read_lines("day_2.txt"):
        list_of_games.append(Game(line))
