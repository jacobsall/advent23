from tqdm import tqdm
f = open("inputs/13.txt")
data = f.read().strip()

test_data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip()

def process(data):
  patterns = data.split("\n\n")
  return [[list(row) for row in pattern.split("\n")] for pattern in patterns]

def transpose(array):
  return [list(row) for row in zip(*array)]

def is_one_char_diff(str1, str2):
  if len(str1) != len(str2):
    return False
  diff_count = sum(1 for a, b in zip(str1, str2) if a != b)
  return diff_count == 1

def score(data, mul=1, p2=False):
  rows = [i for i in range(len(data) - 1)]
  results = []
  for row in rows:
    offset = 0
    diff = 0
    while row - offset >= 0 and row + 1 + offset < len(data):
      if data[row-offset] == data[row+offset+1]:
        offset += 1
      elif p2 and is_one_char_diff(data[row-offset],data[row+offset+1]):
        offset += 1
        diff += 1
      else:
        break
    else:
      if p2 and diff == 1 or not p2:
        results.append((row+1)*mul)
  return results

def part1(data):
  return sum([(score(pattern,100)+score(transpose(pattern)))[0] for pattern in data])


def part2(data):
  return sum([(score(pattern,100, p2=True)+score(transpose(pattern,),p2=True))[0] for pattern in data])


processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))