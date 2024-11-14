import re

file_path = r"2023\input\05-test.txt"


def apply_transformation(source_range : range, destination_range : range, seed):
    # determine the position of the element in the key
    offset =  seed - source_range.start
    # determine the value stored at the same position in corresponding value
    return destination_range.start + offset

    
def part_one() -> int:
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    # use a neater solution
    seeds = [int(seed) for seed in lines[0][6:].split()]

    maps = [{}, {}, {}, {}, {}, {}, {}]
    # use regex to determine these indexes in future.
    #map_starts = [2, 22, 32, 69, 116, 132, 162, 175]  # real input
    map_starts = [2, 6, 11, 17, 21, 26, 30, 34] # test input
    # this can also be cleaned up!
    for i in range(len(map_starts)):
        start = map_starts[i]      
        if i+1 < len(map_starts):
            finish = map_starts[i+1]
            for a in range(start+1, finish-1):
                content = lines[a].split()
                destinatation_range_start = int(content[0])
                source_range_sart = int(content[1])
                range_length = int(content[2])
                source_range = range(source_range_sart, source_range_sart + range_length)
                destination_range = range(destinatation_range_start, destinatation_range_start + range_length)
                maps[i][source_range] =  destination_range

    closest_seed = 0
    minimum_distance = float('inf') 
    # loop through all of the seeds.
    for seed in seeds:
        # initialize the key to the seed value. 
        key = seed
        # loop through the various mappings.
        for map in maps:
            # loop through the ranges in the current mapping
            for source_range in map:
                # if the seed key is in range of the transformation, apply the transformation
                if key in source_range:
                    # if the key is in range, find the value in the associate mapping.
                    key = apply_transformation(source_range, map[source_range], key)
                    break
        if key <= minimum_distance:
            closest_seed = seed
            minimum_distance = key
       
    print(f"Part One: Nearest Location: {minimum_distance}, Closest Seed: {closest_seed}")


def part_two() -> int:
    # for part two we want to reverse the process.    
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = 0
    
    seeds = [int(seed) for seed in lines[0][6:].split()]

    seed_ranges = []
    i = 0
    while i < len(seeds)-1:
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]-1))
        i += 2
    print("Seeds:", seed_ranges)

    # Get all of the location ranges.
    location_ranges = [range(56, 56+37), range(93, 93+4)]
    # Sort location ranges in ascending order.
    sorted_ranges = sorted(location_ranges, key=lambda x: x.start)
    print("Locations:", sorted_ranges)
    # Start at the closest location and find the seed associated with the location
   
    # use regex to determine these indexes in future.
    # map_starts = [2, 22, 32, 69, 116, 132, 162, 175]  # real input
    # Reverse the mapping so we start humidity-to-location map
    
    # use similar code as in part one to build the mappings.

    #
    seed = 0
    for r in sorted_ranges:
        for location in r:
            seed = apply_transformation()
            for seed_range in seed_ranges:
                # check if the seed is in the original list
                if seed in seed_range:

                    break
                    
    print("Part Two:", seed)            

part_one()
part_two()