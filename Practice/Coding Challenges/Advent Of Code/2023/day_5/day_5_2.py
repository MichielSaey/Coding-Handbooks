from enum import Enum
import pandas as pd


class Phase(Enum):
    SEED_TO_SOIL = 1
    SOIL_TO_FERT = 2
    FERT_TO_WAT = 3
    WAT_TO_LIGHT = 4
    LIGHT_TO_TEMP = 5
    TEMP_TO_HUM = 6
    HUM_TO_LOC = 7


def read_lines(filename):
    with open(file=filename) as file:
        for line in file.read().splitlines():
            yield line


class Seed_node:
    start_of_range = 0
    range = 0

    def __init__(self, start_of_range, range):
        self.start_of_range = start_of_range
        self.range = range

    # factory that return al list of new nodes
    # if seed_start <= map_end and map_start <= seed_end pas to factory to create new ranges
    # e.i check for overlap
    # then calculate the overlap, create new nodes, then repeat till there is no more overlap

def build_seed_list(line):
    seeds = line.split(" ")[1:]
    seeds_int = [int(s) for s in seeds]
    seeds = seeds_int

    results = []
    index = 0
    while index < len(seeds):
        results.append(Seed_node(seeds[index], seeds[index + 1]))
        index += 2

    return results

if __name__ == '__main__':
    seeds = []
    data = []
    phase = Phase
    for line in read_lines("day_5_test.txt"):
        if "seeds:" in line:
            seeds = build_seed_list(line)
        elif "seed-to-soil map:" in line:
            phase = Phase.SEED_TO_SOIL
        elif "soil-to-fertilizer map:" in line:
            phase = Phase.SOIL_TO_FERT
        elif "fertilizer-to-water map:" in line:
            phase = Phase.FERT_TO_WAT
        elif "water-to-light map:" in line:
            phase = Phase.WAT_TO_LIGHT
        elif "light-to-temperature map:" in line:
            phase = Phase.LIGHT_TO_TEMP
        elif "temperature-to-humidity map:" in line:
            phase = Phase.TEMP_TO_HUM
        elif "humidity-to-location map:" in line:
            phase = Phase.HUM_TO_LOC
        elif line == "":
            continue
        else:
            values = line.strip().split(" ")
            destination_range_start, source_range_start, range_length = values
            destination_range_start, source_range_start, range_length = int(destination_range_start), int(source_range_start), int(range_length)
            columns = {
                'Phase': phase.name,
                'Source_range_start': source_range_start,
                'Source_range_end': source_range_start + range_length,
                'Destination_range_start': destination_range_start,
                'Destination_range_end': destination_range_start + range_length,
                'Range': range_length
            }
            data.append(columns)

    df = pd.DataFrame(data)
    print(df.to_string(), "\n")

    for phase in Phase:
        print(f"PHASE: {phase.name}")
        print(f"Seed: {seeds}", "\n")
        filter_phase = df['Phase'] == phase.name
        filter_df = df.where(filter_phase)
        filter_df.dropna(inplace=True)
        for seed in seeds:
            # repace seeds every phase whit the new ly calculated notes


    # TODO:
    #  Stop using the array of seeds but use the result table
    #  Id seed by index in table and all the transaction that are made to it
    #  calculate using ranges, that can split of from each other?
    #  Turn into object with id, start range's and end ranges's after each map.
    #  tree... turn it into a tree