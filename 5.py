import math
f = open("inputs/5.txt")
data = f.read().strip()

test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip()

def process(data):
  parts = data.split("\n\n")

  seeds = [int(x) for x in parts[0].split(":")[1].split()]

  def parse_map(map):
    lines = map.split("\n")
    return [[int(x) for x in line.split()] for line in lines]
  
  mappings = [parse_map(x.split(":")[1].strip()) for x in parts[1:]]
  return (seeds, mappings)


def part1(data):
  def do_lookup(ranges, num):
    for r in ranges:
      if r[1] <= num <= r[1] + r[2]:
        return r[0] + num - r[1]
    return num

  seeds, mappings = data
  res = []
  for seed in seeds:
    temp_res = [seed]
    for mapping in mappings:
      temp_res.append(do_lookup(mapping, temp_res[-1]))
    res.append(temp_res)
  return min([x[-1] for x in res])

def part2(data):
  seeds, mappings = data
  seed_ranges = []
  i = 0
  while i < len(seeds):
    f = seeds[i]
    t = seeds[i+1] + f - 1
    seed_ranges.append((f,t))
    i += 2

  answer = math.inf
  for seed_range in seed_ranges:
    ranges = [seed_range]
    for mapping in mappings:
      processed_ranges = []
      while len(ranges):
        range_from, range_to  = ranges.pop()
        for dest, source, length in mapping:
          offset = dest - source
          end = source + length 
          if range_to <= source or end <= range_from:
            continue
          if range_from < source:
            ranges.append((range_from, source))
            range_from = source
          if end < range_to:
            ranges.append((end, range_to))
            range_to = end
          processed_ranges.append((range_from + offset, range_to + offset))
          break
        else:
          processed_ranges.append((range_from, range_to))
      ranges = processed_ranges
    answer = min(answer, min(a for a,_ in ranges))
  return answer

processed = process(data)

print("part 1", part1(processed))
print("part 2", part2(processed))