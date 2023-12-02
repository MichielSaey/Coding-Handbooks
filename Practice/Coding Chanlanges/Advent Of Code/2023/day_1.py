from builtins import len

file = open(file="day_1.txt")


# 1. Take each line
# 2. Make a number from the first and last digit
# 3. Add that number to the result.
# 4. Repeat

def calibrate_trebuchet():
    result = 0
    first_digit = ""
    next_digit = ""
    line_number = 1
    for char in file.read():
        if char.isdigit():
            if first_digit == "":
                first_digit = char
            next_digit = char
        elif char == "\n":
            line_result = first_digit + next_digit
            line_number += 1
            result += int(line_result)
            first_digit = ""
            next_digit = ""
    line_result = first_digit + next_digit
    line_number += 1
    result += int(line_result)
    return result


# print(calibrate_trebuchet())


# Part 2

# Dictonaire of all searched chars
# Alternative on KMP

def computeSigmaTable(line: str):
    # output
    sigma_table = [0] * len(line)

    # variables
    index_in_table = 2
    index_in_word = 0

    while index_in_table < len(line):
        if line[index_in_table] == line[index_in_word]:
            index_in_table = index_in_table + 1
            index_in_word = index_in_word + 1
            sigma_table[index_in_table] = index_in_word
        elif index_in_word > 0:
            index_in_word = sigma_table[index_in_word]
        else:  # k = 0
            sigma_table[index_in_table] = 0
            index_in_table = index_in_table + 1

    return sigma_table


def KMPSearch(line: str, word: str):
    # output
    match_position = [0]
    match_count = 0

    # variables
    index_in_line = 0
    index_in_word = 0
    sigma_table: [] = computeSigmaTable(line)

    while index_in_line < len(line):
        if line[index_in_line] == word[index_in_word]:
            index_in_line += 1
            index_in_word += 1
            if index_in_word == len(word):  # Check if there is a full match
                match_position[match_count] = index_in_line - index_in_word
                match_count = match_count + 1
                index_in_word = sigma_table[index_in_word]
        else:
            index_in_word = sigma_table[index_in_word]
            if index_in_word <= 0:
                index_in_line = index_in_line + 1
                index_in_word = index_in_word + 1

    return match_position


print(KMPSearch("7pqrstsixteen", "six"))
