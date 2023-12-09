import re
from enum import Enum

def read(filename):
    with open(file=filename) as file:
        for char in file.read():
            yield char


def find_symbols(schematic):
    x_axes = 0
    while x_axes < len(schematic):
        y_axes = 0
        while y_axes < len(schematic[x_axes]):
            schematic_element = schematic[x_axes][y_axes]
            if re.search(r"[-=#*@%/+&$]", schematic_element):
                yield [x_axes, y_axes]
            y_axes += 1
        x_axes += 1


class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    BIDIRECTIONAL = 3

def digit_crawler(line: str, start_point: int, direction: Direction = Direction.FORWARD):
    digit = ""
    is_digit = True
    while is_digit:
        if line[start_point].isdigit():
            digit += line[start_point]
            start_point = start_point + 1 if direction == Direction.FORWARD else start_point - 1
        else:
            is_digit = False

    if direction == Direction.BACKWARD:
        digit = digit[::-1]
    if direction == Direction.BIDIRECTIONAL: # and if digit is not zero reverse it, and redo with a forward functionloop
        digit = digit[::-1]
    return int(digit) if digit.isdigit() else 0


def sum_of_surrounding_numbers(schematic, symbol):
    # first get numbers form left and right
    result = 0
    # Left
    result += digit_crawler(schematic[symbol[0]], symbol[1] - 1, Direction.BACKWARD)

    # Right
    result += digit_crawler(schematic[symbol[0]], symbol[1] + 1, Direction.FORWARD)

    # Middle top
    middle_top_result += digit_crawler(schematic[symbol[0] - 1], symbol[1], Direction.BIDIRECTIONAL)
    # 1. Start in the middle,
    # 2. if digit do bidirectional
    # 3. if no run crawler on top left en top right


    print(schematic[symbol[0] - 1][symbol[1] - 1], schematic[symbol[0] - 1][symbol[1]], schematic[symbol[0] - 1][symbol[1] + 1])
    print(schematic[symbol[0]][symbol[1] - 1], schematic[symbol[0]][symbol[1]], schematic[symbol[0]][symbol[1] + 1])
    print(schematic[symbol[0] + 1][symbol[1] - 1], schematic[symbol[0] + 1][symbol[1]], schematic[symbol[0] + 1][symbol[1] + 1])
    return result0


if __name__ == '__main__':
    schematic = []
    line_array = []
    for char in read("day_3.txt"):
        if char == '\n':
            schematic.append(line_array)
            line_array = []
        else:
            line_array.append(char)

    result = 0
    for symbol in find_symbols(schematic):
        result += sum_of_surrounding_numbers(schematic, symbol)
