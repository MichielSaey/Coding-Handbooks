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

    def set_color_count(self, color, amount):
        match color:
            case re.match(r"+red+", color):
                self.set_red(int(amount))
            case re.match(r"+green+", color):
                self.set_green(int(amount))
            case re.match(r"+blue+", color):
                self.set_blue(int(amount))


class Game:
    def __init__(self, line):
        line_prifex = line.split(":")[0]
        self.id = line_prifex.split(" ")[1]
        self.sets = []
        line_sets = line.split(":")[1]
        for line_set in line_sets.split(";"):
            set = Set()
            for game_line in line_set.split(","):
                game_line = game_line.strip()
                color = game_line.split(" ")[1]
                amount = game_line.split(" ")[0]
                set.set_color_count(color, amount)
            print(set)




if __name__ == '__main__':
    list_of_games = []
    for line in read_lines("day_2.txt"):
        list_of_games.append(Game(line))
