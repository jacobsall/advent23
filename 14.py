f = open("inputs/14.txt")
data = f.read().strip()

test_data = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip()

directions = ["up", "left", "down", "right"]

def process(data):
  return [list(line) for line in data.split("\n")]

def transpose(array):
  return [list(row) for row in zip(*array)]

def tilt(data, d="up"):
  vertical = d in ["up", "down"]
  flip = d in ["down", "right"]
  grid = transpose(data) if vertical else data.copy()
  for i, row in enumerate(grid):
    splits = str(row).split("#") if not flip else str(row[::-1]).split("#")
    replacement = ""
    for split in splits:
      replacement += "O" * split.count("O") + "." * split.count(".") + "#"
    replacement = replacement[:-1]
    grid[i] = list(replacement[:]) if not flip else list(replacement[::-1])
  return transpose(grid) if vertical else grid
  
def calc(grid):
  res = []
  for y, row in enumerate(grid):
    count = 0
    for x, cell in enumerate(row):
      if cell == "O":
        count += len(grid[y]) - y
    res.append(count)
  return sum(res)

def part1(data):
  grid = tilt(data, "up")
  return calc(grid)

def part2(data):
  grid = data
  seen_grids = {str(data): 0}
  t,f = 0,0
  
  for i in range(1000000000):
    for d in directions:
      grid = tilt(grid, d)
    grid_str = str(grid)
    if grid_str in seen_grids:
      t,f = i, seen_grids[grid_str]
      break
    else:
      seen_grids[grid_str] = i

  cycle_len = t - f
  res = (1000000000 - 1 - f) % cycle_len

  for i in range(res):
    for d in directions:
      grid = tilt(grid, d)
  return calc(grid)

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))