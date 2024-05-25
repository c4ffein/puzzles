# Copyright (c) c4ffein
# Check https://github.com/c4ffein/puzzles/blob/main/LICENSE for license
# Check https://github.com/c4ffein/puzzles/blob/main/README.md before judging code quality


import math


with open("input.txt") as f:
    i = f.read()
categories = i[:-1].split("\n\n")


seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


name_to_ds = {
    "seed-to-soil": seed_to_soil,
    "soil-to-fertilizer": soil_to_fertilizer,
    "fertilizer-to-water": fertilizer_to_water,
    "water-to-light": water_to_light,
    "light-to-temperature": light_to_temperature,
    "temperature-to-humidity": temperature_to_humidity,
    "humidity-to-location": humidity_to_location,
}


for category in categories:
    ls = category.split("\n")
    ds_name = ls[0].split(" ")[0]
    if ds_name == "seeds:":
        seeds = [int(s) for s in ls[0].split(" ")[1:]]
        continue
    for l in ls[1:]:
        l_destination, l_source, l_range = [int(s) for s in l.split()]
        name_to_ds[ds_name].append([[l_source, l_source + l_range - 1], l_destination - l_source])

min_end_fids = math.inf
for seed in seeds:
    fid = seed
    for conversion_name, conversions_maps in name_to_ds.items():
        for (range_start, range_end), move in conversions_maps:
            if range_start <= fid <= range_end:
                fid += move
                break
        # No else : if unmapped, keep id
    min_end_fids = min(min_end_fids, fid)
print(min_end_fids)

# V2
for ds in name_to_ds.values():
    ds.sort(key=lambda e: e[0][0])

limits_ranges = [[ran[0], ran[0] + ran[1] - 1] for ran in zip(seeds[0::2], seeds[1::2])]
for converter in name_to_ds.values():
    new_limits_ranges = []
    for limits_range_start, limits_range_end in limits_ranges:
        points = []
        started = None
        ended = False
        for (conversion_start, conversion_end), offset in converter:
            if conversion_start < limits_range_start <= limits_range_end < conversion_end:
                points = [[limits_range_start, offset], [limits_range_end, offset]]
                started = ended = True
                break
            if limits_range_start <= conversion_start <= limits_range_end:
                points.append([conversion_start, offset])
                ended = False
                started = True if started is None else started
            if limits_range_start <= conversion_end <= limits_range_end:
                points.append([conversion_end, offset])
                started = False if started is None else started
                ended = True
        else:
            if len(points) == 0:
                new_limits_ranges.append([limits_range_start, limits_range_end])
                continue
            if not started:
                points = [[limits_range_start, points[0][1]], *points]
            if not ended:
                points = [*points, [limits_range_end, points[-1][1]]]
            i = 1
            while i + 1 < len(points):
                if points[i][0] != points[i+1][0] - 1:
                    points = points[:i+1] + [[points[i][0] + 1, 0], [points[i+1][0] - 1, 0]] + points[i+1:]
                i += 2
            if points[0][0] != limits_range_start:
                points = [[limits_range_start, 0], [points[0][0] - 1, 0], *points]
            if points[-1][0] != limits_range_end:
                points = [*points, [points[-1][0] + 1, 0], [limits_range_end, 0]]
        for i in range(0, len(points), 2):
            offset = points[i][1]
            assert offset == points[i+1][1]
            new_limits_ranges.append(sorted([points[i][0] + offset, points[i+1][0] + offset]))
    limits_ranges = []
    if len(new_limits_ranges) == 0:
        continue
    new_limits_ranges = sorted(new_limits_ranges)
    limits_ranges = [new_limits_ranges[0]]
    for limit_range in new_limits_ranges[1:]:
        if limits_ranges[-1][1] + 1 >= limit_range[0]:
            limits_ranges[-1][1] = max(limit_range[1], limits_ranges[-1][1])
        else:
            limits_ranges.append(limit_range)
print(min(e[0] for e in limits_ranges))
