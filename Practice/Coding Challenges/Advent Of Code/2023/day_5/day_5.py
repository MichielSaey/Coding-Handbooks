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

if __name__ == '__main__':
    seeds = []
    data = []
    phase = Phase
    for line in read_lines("day_5_test.txt"):
        if "seeds:" in line:
            seeds = line.split(" ")[1:]
            print(seeds)
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
            columns= {
                'Phase': phase,
                'Range_start': destination_range_start,
                'Source_range_start': source_range_start,
                'Range': range_length
            }
            data.append(columns)

    df = pd.DataFrame(data)
    print(df)

    for phase in Phase:
        filter_phase = df['Phase'] == phase
        filter_df = df.where(filter_phase)
        filter_df.dropna(inplace=True)
        for seed in seeds:
            filter_seeds_start = df['Range_start'] <= seed
            filter_seed_end = seed <= df['Range_start'] + df['Range']
            filter_df = filter_df.where(filter_seeds_start, filter_seed_end)
            filter_df.dropna(inplace=True)
            print(f"Seed: {seed}, phase: {phase}")
            if filter_df.empty:
                print("No map found")
            else:
                print(filter_df)

