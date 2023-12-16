from tqdm import tqdm
f = open("inputs/16.txt")
data = f.read().strip()

test_data = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""".strip()

def process(data):
  return [list(line) for line in data.split("\n") if line != ""]

def traverse(grid, x, y, dx, dy, visited):
  while y < len(grid) and x >= 0 and x < len(grid[y]) and y >= 0 and (x,y,dx,dy) not in visited:
    visited.add((x,y,dx,dy))
    if grid[y][x] == "|" and (dx,dy) in [(1,0),(-1,0)]:
      traverse(grid, x, y, 0, -1, visited)
      traverse(grid, x, y, 0, 1, visited)
      break
    elif grid[y][x] == "-" and (dx,dy) in [(0,1),(0,-1)]:
      traverse(grid, x, y, 1, 0, visited)
      traverse(grid, x, y, -1, 0, visited)
      break
    elif grid[y][x] == "\\":
      dx,dy = dy,dx
    elif grid[y][x] == "/":
      dx,dy = -dy,-dx
    x += dx
    y += dy

def only_pos(visited):
    return set((x, y) for x,y,_,_ in visited)

def part1(grid, x=0, y=0, dx=1, dy=0):
  grid = grid.copy()
  visited = set()
  traverse(grid, x, y, dx, dy, visited)
  return len(only_pos(visited))

def part2(data):
  totals = []
  for i in tqdm(range(len(data[0]))):
    totals.append(part1(data, i, 0, 0, 1))
    totals.append(part1(data, i, len(data)-1, 0, -1))
  for j in tqdm(range(len(data))):
    totals.append(part1(data, 0, j, 1, 0))
    totals.append(part1(data, len(data[0]), j, -1, 0))
  return max(totals)

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))