import math


def read_lines(filename):
    with open(file=filename) as file:
        for line in file.read().splitlines():
            yield line


def build_array_from_line(line):
    array_elements = line.split(":")[1]
    array_elements = list(filter(lambda element: element != "", array_elements.split(" ")))
    array_elements = [int(s) for s in array_elements]
    return array_elements


def build_digit_from_line(line):
    race_number = ""
    array_elements = line.split(":")[1]
    array_elements = list(filter(lambda element: element != "", array_elements.split(" ")))
    for s in array_elements:
        race_number += s
    return int(race_number)


def read_input(file):
    times = []
    distances = []
    for line in read_lines(file):
        if "Time:" in line:
            # times = build_array_from_line(line)
            times = build_digit_from_line(line)
        elif "Distance:" in line:
            # distances = build_array_from_line(line)
            distances = build_digit_from_line(line)

    if type(times) == list:
        return [(times[i], distances[i]) for i in range(0, len(times))]
    else:
        return [(times, distances)]


def cal_nr_wins(time, record):
    nr_of_wins = 0

    for press_time in range(time):
        possible_distance = press_time * (time - press_time)
        if possible_distance > record:
            nr_of_wins += 1

    print(f"For a race with time of {time} and a record of {record}, there are {nr_of_wins} possible ways to win.")
    return nr_of_wins


def cal_win_margin(races):
    margin = 1
    for time, record in races:
        margin *= cal_nr_wins(time, record)

    return margin


if __name__ == '__main__':
    races = read_input("day_6.txt")
    print(races)
    print(cal_win_margin(races))
