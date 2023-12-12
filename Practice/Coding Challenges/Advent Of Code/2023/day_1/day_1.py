from builtins import len

file = open(file="input.txt")


# 1. Take each line
# 2. Make a number from the first and last digit
# 3. Add that number to the result.
# 4. Repeat

def calibrate_trebuchet():
    result = 0
    first_digit = ""
    next_digit = ""
    for char in file.read():
        if char.isdigit():
            if first_digit == "":
                first_digit = char
            next_digit = char
        elif char == "\n":
            line_result = first_digit + next_digit
            result += int(line_result)
            first_digit = ""
            next_digit = ""
    line_result = first_digit + next_digit
    result += int(line_result)
    return result


# print(calibrate_trebuchet())


# Part 2

# Dictonaire of all searched chars
# Make it usable like a string
# function to add
# * equels
# * len
# * return match as int
class Dictionary:
    def __init__(self):
        # Dictionary of all numbers
        self.dictionary_of_digits = {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
            'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0,
        }

        # Dictionary of all possible items, will shrink after every equals
        self.dictionary_of_possible_digits = self.dictionary_of_digits
        self.first_match = "0"
        self.next_match = "0"
        self.match_count = 0
        self.matches = []

    def __len__(self):
        # Return the longest element in the possible options
        longest_key = list(self.dictionary_of_possible_digits.keys())
        longest_key.sort(key=len)
        longest_key = longest_key[0]
        return len(longest_key)

    def equal(self, other, index):
        # check if in the dictionary, there is a char matching the other char, on the same index
        # keys_with_match = filter(lambda key: key[index] == other, self.dictionary_of_digits.keys())
        keys_with_match = []
        for key in self.dictionary_of_possible_digits.keys():
            if index >= len(key):
                continue
            char = key[index]
            if char == other:
                keys_with_match.append(key)

        if len(list(keys_with_match)) == 0:
            self.dictionary_of_possible_digits = self.dictionary_of_digits.copy()
            return False

        keys_with_match = list(keys_with_match)
        self.dictionary_of_possible_digits = {}
        for key in keys_with_match:
            self.dictionary_of_possible_digits[key] = self.dictionary_of_digits[key]
        return True

    def match(self):
        match = list(self.dictionary_of_possible_digits.keys())[0]
        if self.first_match == "0":
            self.first_match = match
        self.next_match = match
        self.dictionary_of_possible_digits = self.dictionary_of_digits

        self.match_count += 1
        self.matches.append(match)

    def get_value(self):
        first_digit = self.dictionary_of_digits.get(self.first_match) * 10
        last_digit = self.dictionary_of_digits.get(self.next_match)
        return first_digit + last_digit


def kmp_search(line: str):
    # input
    word = Dictionary()

    # variables
    index_in_line = 0
    index_in_word = 0
    # I had a simga table in here, but realised i did not fucking mather

    while index_in_line < len(line):
        char = line[index_in_line]
        if word.equal(line[index_in_line], index_in_word):
            index_in_word += 1
            length_word = len(word)
            if index_in_word == length_word:  # Check if there is a full match
                word.match()
                index_in_word = 0
                if length_word <= 1 or not word.equal(line[index_in_line], 0):
                    index_in_line = index_in_line + 1
            else:
                index_in_line = index_in_line + 1
        elif index_in_line > 1 and word.equal(line[index_in_line - 1], 0) and word.equal(line[index_in_line], 1):
            index_in_line = index_in_line - 1
            index_in_word = 0
        elif word.equal(line[index_in_line], 0):
            index_in_word = 0
        else:
            index_in_word = 0
            index_in_line = index_in_line + 1

    return word.get_value()

# print(kmp_search("snqhqmffonettwofourgdkjmbjvjpgxxxpzkm8zfpfcgj"))

def calibrate_trebuchet_2():
    result = 0
    for line in file.read().splitlines():
        new_result = kmp_search(line) + result
        print(line, ": ", new_result - result)
        result = new_result
    return result


print(calibrate_trebuchet_2())
