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
    seeds_int = [int(s) for s in seeds]
    seeds = seeds_int

    results = []

    print(f"starting seeds:", seeds)

    index = 0
    while index < len(seeds):
        for x in range(seeds[index], seeds[index] + seeds[index + 1]):
            if x not in results:
                results.append(x)
        print(results)
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

    results_df = pd.DataFrame()
    results_df['Start'] = seeds

    for phase in Phase:
        print(f"PHASE: {phase.name}")
        print(f"Seed: {seeds}", "\n")
        filter_phase = df['Phase'] == phase.name
        filter_df = df.where(filter_phase)
        filter_df.dropna(inplace=True)
        for seed in seeds:
            filter_seeds = (df['Source_range_start'] <= seed) & (seed < df['Source_range_end'])
            seed_filtered_df = filter_df.where(filter_seeds)

            seed_filtered_df.dropna(inplace=True)
            if seed_filtered_df.empty:
                print(f"No map found for seed: {seed}, so it keeps the same value!", "\n")
                continue

            print(seed_filtered_df.to_string())
            seed_modifier = seed - seed_filtered_df.iloc[0]['Source_range_start']
            seed_modifier = int(seed_modifier)
            new_value = seed_filtered_df.iloc[0]['Destination_range_start'] + seed_modifier
            new_value = int(new_value)
            print(f"Seed {seed} modified by map: {seed_filtered_df.iloc[0]['Source_range_start']} + {seed_modifier} = {new_value}", '\n')
            seeds[seeds.index(seed)] = new_value

        results_df[phase.name] = seeds

    print("Final state of seeds:", seeds)
    print(results_df.to_string())
    print("\n")


