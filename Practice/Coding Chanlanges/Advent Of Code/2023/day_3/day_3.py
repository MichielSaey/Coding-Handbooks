import re

def read(filename):
    with open(file=filename) as file:
        for char in file.read():
            yield char


def find_symbols(schematic):
    x_axes = 0
    y_axes = 0
    while x_axes < len(schematic):
        while y_axes < len(schematic[x_axes]):
            if re.search(r"[-=#*@%/+&$]", schematic[x_axes][y_axes]):
                return [x_axes, y_axes]


def sum_of_surounding_nummbers(schematic, symbol):
    pass


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
        result += sum_of_surounding_nummbers(schematic, symbol)
        

    for line in schematic:
        string_builder = ""
        for char in line:
            string_builder += " " + char + " "
        print(f'{string_builder}')