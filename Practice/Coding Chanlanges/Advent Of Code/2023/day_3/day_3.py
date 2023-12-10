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
    index_in_line = start_point
    while True:
        if line[index_in_line].isdigit():
            digit += line[index_in_line]
            index_in_line = index_in_line + 1 if direction == Direction.FORWARD else index_in_line - 1
        else:
            break

    if direction == Direction.BACKWARD and digit != "":
        digit = digit[::-1]
    elif direction == Direction.BIDIRECTIONAL and digit != "":
        # and if digit is not zero reverse it, and redo with a forward functionloop
        digit = digit[::-1]
        # TODO: This function might return a 0 if nothing is found, but also if a zero is found. might need to return to
        # none return in case of of nothing, and the check it each time...
        # Or overwrite the standard entity type for None Or create new one with add magic function
        other_side_result = digit_crawler(line, start_point + 1, direction.FORWARD)
        if other_side_result != 0:
            digit += str(other_side_result)
    return int(digit) if digit.isdigit() else None


def sum_of_surrounding_numbers(schematic, symbol):
    # Left
    result = digit_crawler(schematic[symbol[0]], symbol[1] - 1, Direction.BACKWARD)

    # Middle top
    top_middle_result = digit_crawler(schematic[symbol[0] - 1], symbol[1], Direction.BIDIRECTIONAL)
    if top_middle_result != 0:
        result += top_middle_result
    else:
        result += digit_crawler(schematic[symbol[0] - 1], symbol[-1], Direction.BACKWARD)
        result += digit_crawler(schematic[symbol[0] - 1], symbol[1], Direction.FORWARD)

    # Right
    result += digit_crawler(schematic[symbol[0]], symbol[1] + 1, Direction.FORWARD)

    # Middle bottom
    bottom_middle_result = digit_crawler(schematic[symbol[0] + 1], symbol[1], Direction.BIDIRECTIONAL)
    if bottom_middle_result  != 0:
        result += bottom_middle_result
    else:
        result += digit_crawler(schematic[symbol[0] + 1], symbol[-1], Direction.BACKWARD)
        result += digit_crawler(schematic[symbol[0] + 1], symbol[1], Direction.FORWARD)

    return result


if __name__ == '__main__':
    schematic = []
    line_array = []
    for char in read("day_3.txt"):
        if char == '\n':
            schematic.append(line_array)
            line_array = []
            continue
        line_array.append(char)
    schematic.append(line_array)

    result = 0
    for symbol in find_symbols(schematic):
        result += sum_of_surrounding_numbers(schematic, symbol)

    print(result)