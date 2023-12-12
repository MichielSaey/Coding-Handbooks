def read_lines(filename):
    with open(file=filename) as file:
        for line in file.read().splitlines():
            yield line


class Set:
    red = 0
    green = 0
    blue = 0

    def __str__(self):
        return f"Red: {self.red}, Green: {self.green}, Blue:{self.blue}"

    def set_red(self, red_amount):
        self.red = red_amount

    def set_green(self, green_amount):
        self.green = green_amount

    def set_blue(self, blue_amount):
        self.blue = blue_amount

    def set_color_count(self, color, amount):
        match color:
            case "red":
                self.set_red(int(amount))
            case "green":
                self.set_green(int(amount))
            case "blue":
                self.set_blue(int(amount))

    def validate(self, red, green, blue):
        if self.red > red:
            return False
        if self.green > green:
            return False
        if self.blue > blue:
            return False
        return True


class Game:
    def __init__(self, line):
        line_prefix = line.split(":")[0]
        self.id = line_prefix.split(" ")[1]
        self.sets = []
        line_sets = line.split(":")[1]
        for line_set in line_sets.split(";"):
            set = Set()
            for game_line in line_set.split(","):
                game_line = game_line.strip()
                color = game_line.split(" ")[1]
                amount = int(game_line.split(" ")[0])
                set.set_color_count(color, amount)
            self.sets.append(set)

    def __str__(self):
        string_builder = f"Game {self.id}\n"
        for set in self.sets:
            string_builder += str(set)
            string_builder += "\n"

        return string_builder

    def validate(self, red, green, blue):
        validation = True
        index = 0
        while validation and index < len(self.sets):
            validation = self.sets[index].validate(red, green, blue)
            index += 1
        return validation

    def calculate_power(self):
        largest_set = self.get_largest_possible_set()
        return largest_set.blue * largest_set.red * largest_set.green

    def get_largest_possible_set(self):
        largest_set = Set()
        for set in self.sets:
            if set.blue > largest_set.blue:
                largest_set.set_blue(set.blue)
            if set.red > largest_set.red:
                largest_set.set_red(set.red)
            if set.green > largest_set.green:
                largest_set.set_green(set.green)
        return largest_set


if __name__ == '__main__':
    list_of_games = []
    for line in read_lines("day_2.txt"):
        list_of_games.append(Game(line))

    result = 0
    for game in list_of_games:
         result += game.calculate_power()

    print(result)
