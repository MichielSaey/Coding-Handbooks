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


def build_seed_list(line):
    seeds = line.split(" ")[1:]

    results = []
    index = 0
    while index < len(seeds):
        # Tuple (start, range)
        results.append((int(seeds[index]), int(seeds[index + 1])))
        index += 2

    return results


def calculate_overlap(seed_start, seed_range, ranges_of_maps):
    new_seeds = []

    end_of_seed = seed_start + seed_range
    ranges_of_maps.append((seed_start, seed_range, 0))

    for index, (start, range, modifier) in enumerate(ranges_of_maps):
        new_start = None
        new_range = None

        # find new start
        if start + range > seed_start and seed_start >= start:
            new_start = seed_start  # Start of new mapped range when the mapped range starts before the seed
        elif seed_start < start and start + range < seed_start + seed_range:
            new_start = start  # Start of new mapped range when mapped range starts after seed start
            new_seeds.append((seed_range, new_start - seed_start))  # Remainder range before

        # find new end
        if new_start and seed_start + seed_range <= start + range:
            new_range = (seed_start + seed_range) - new_start
            seed_start = (seed_start + seed_range)
            seed_range = 0
        elif new_start:
            new_range = (start + range) - new_start
            seed_start = (start + range)
            seed_range = end_of_seed - seed_start

        if new_start and new_range:
            new_seeds.append((new_start + modifier, new_range))

    return new_seeds


def map_seeds(df, seeds):
    data_tracking = pd.DataFrame()
    print(f"PHASE: Start")
    print(seeds)

    for phase in Phase:
        # get phase maps
        print(f"PHASE: {phase.name}")
        filter_phase = df['Phase'] == phase.name
        filter_df = df.where(filter_phase)
        filter_df.dropna(inplace=True)

        # loop over seeds
        new_seeds = []
        for seed_start_of_range, seed_range in seeds:
            ranges_of_maps = sorted([row for row in
                                     filter_df[['Source_range_start', 'Range', 'Modifier']].itertuples(index=False,
                                                                                                       name=None)],
                                    key=lambda x: x[0])

            new_seeds.extend(calculate_overlap(seed_start_of_range, seed_range, ranges_of_maps))

        seeds = new_seeds
        print(seeds)
        print("end of phase")

    print("PHASE: End")

    df = pd.DataFrame(seeds, columns =['Start', 'Range'])

    print(df.to_string())


if __name__ == '__main__':
    seeds = []
    data = []
    phase = Phase
    for line in read_lines("day_5.txt"):
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
            destination_range_start, source_range_start, range_length = int(destination_range_start), int(
                source_range_start), int(range_length)
            columns = {
                'Phase': phase.name,
                'Source_range_start': source_range_start,
                'Source_range_end': source_range_start + range_length,
                'Modifier': destination_range_start - source_range_start,
                'Destination_range_start': destination_range_start,
                'Destination_range_end': destination_range_start + range_length,
                'Range': range_length
            }
            data.append(columns)

    df = pd.DataFrame(data)
    print(df.to_string(), "\n")
    map_seeds(df, seeds)
