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


def find_gear(schematic):
    x_axes = 0
    while x_axes < len(schematic):
        y_axes = 0
        while y_axes < len(schematic[x_axes]):
            schematic_element = schematic[x_axes][y_axes]
            if re.search(r"[*]", schematic_element):
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
    while len(line) > index_in_line >= 0:
        if line[index_in_line].isdigit():
            digit += line[index_in_line]
            index_in_line = index_in_line + 1 if direction == Direction.FORWARD else index_in_line - 1
        else:
            break

    if direction == Direction.BACKWARD and digit != "":
        digit = digit[::-1]
    elif direction == Direction.BIDIRECTIONAL and digit != "":
        # and if digit is not zero reverse it, and redo with a forward function loop
        digit = digit[::-1]
        forward_result = digit_crawler(line, start_point + 1, direction.FORWARD)
        digit += str(forward_result) if forward_result else ""
    return digit if digit.isdigit() else None


def sum_of_surrounding_numbers(schematic, symbol, required_amount_of_numbers = 0):
    surrounding_numbers = []

    # Left
    middle_left_result = digit_crawler(schematic[symbol[0]], symbol[1] - 1, Direction.BACKWARD)
    if middle_left_result:
        surrounding_numbers.append(int(middle_left_result))
    # Middle top
    top_middle_result = digit_crawler(schematic[symbol[0] - 1], symbol[1], Direction.BIDIRECTIONAL)
    if top_middle_result:
        surrounding_numbers.append(int(top_middle_result))
    else:
        top_left_result = digit_crawler(schematic[symbol[0] - 1], symbol[1] - 1, Direction.BACKWARD)
        if top_left_result:
            surrounding_numbers.append(int(top_left_result))
        top_right_result = digit_crawler(schematic[symbol[0] - 1], symbol[1] + 1, Direction.FORWARD)
        if top_right_result:
            surrounding_numbers.append(int(top_right_result))

    # Right
    middle_right_result = digit_crawler(schematic[symbol[0]], symbol[1] + 1, Direction.FORWARD)
    if middle_right_result:
        surrounding_numbers.append(int(middle_right_result))

    # Middle bottom
    bottom_middle_result = digit_crawler(schematic[symbol[0] + 1], symbol[1], Direction.BIDIRECTIONAL)
    if bottom_middle_result:
        surrounding_numbers.append(int(bottom_middle_result))
    else:
        bottom_left_result = digit_crawler(schematic[symbol[0] + 1], symbol[1] - 1, Direction.BACKWARD)
        if bottom_left_result:
            surrounding_numbers.append(int(bottom_left_result))
        bottom_right_result = digit_crawler(schematic[symbol[0] + 1], symbol[1] + 1, Direction.FORWARD)
        if bottom_right_result:
            surrounding_numbers.append(int(bottom_right_result))

    if len(surrounding_numbers) == required_amount_of_numbers:
        product_of_surrounding_numbers = 1
        for result in surrounding_numbers:
            product_of_surrounding_numbers *= result
        return product_of_surrounding_numbers
    return 0


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
    for symbol in find_gear(schematic):
        result += sum_of_surrounding_numbers(schematic, symbol, 2)

    print(result)
