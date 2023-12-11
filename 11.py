from tqdm import tqdm
from itertools import combinations
f = open("inputs/11.txt")
data = f.read().strip()

test_data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()

def process(data):
  grid = [list(line) for line in data.split("\n")]
  new_grid = []

  for row in grid:
    if '#' not in row:
      new_grid.append(['.'] * len(row))
    new_grid.append(row)

  num_cols = len(new_grid[0])
  cols_to_insert = []
  for col_idx in range(num_cols):
    if all(row[col_idx] != '#' for row in new_grid):
      cols_to_insert.append(col_idx)

  for col_idx in reversed(cols_to_insert):
    for row in new_grid:
      row.insert(col_idx, '.')

  idcs = [(i, j) for i, row in enumerate(new_grid) for j, char in enumerate(row) if char == '#']
  pairs = list(combinations(idcs, 2))
  return new_grid, pairs

def manhattan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def part1(data):
  grid, pairs = data
  finished = []
  for pair in tqdm(pairs):
    finished.append(manhattan(pair[0][0], pair[0][1], pair[1][0], pair[1][1]))
  return sum(finished)

def part2(data):
  grid, pairs = data
  distance = 0
  for pair in tqdm(pairs):
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    dist = manhattan(x1, y1, x2, y2)
    for i in range(min(x1, x2) + 1, max(x1, x2)):
        if all(grid[i][j] == '.' for j in range(len(grid[i]))):
            dist += 1000000//2-1 # 1000000//2-1 is to account for the doubling in the data processing for part 1 :)
    for j in range(min(y1, y2) + 1, max(y1, y2)):
        if all(grid[i][j] == '.' for i in range(len(grid))):
            dist += 1000000//2-1
    distance += dist
  return distance

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))