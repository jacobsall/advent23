from tqdm import tqdm
f = open("inputs/10.txt")
data = f.read().strip()

test_data = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip()

test_data2 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip()

def get_path(graph, start):
  path = [start, graph[start].pop()]
  while True:
    n = [x for x in graph[path[-1]] if x not in path]
    if not n:
      break
    path.append(n.pop())
  return path

def process(data):
  grid = [list(lines) for lines in data.split("\n")]
  graph = {(x,y) : set() for y in range(len(grid)) for x in range(len(grid[y]))}
  start = None

  r_adj = ["J", "-", "7", "S"]
  l_adj = ["F", "-", "L", "S"]
  u_adj = ["7", "|", "F", "S"]
  d_adj = ["J", "|", "L", "S"]

  for y in range(len(grid)):
    for x in range(len(grid[y])):
      current = grid[y][x]
      if current == "|":
        if y > 0 and grid[y-1][x] in u_adj:
          graph[(x, y)].add((x, y - 1))
          graph[(x, y-1)].add((x, y))
        if y < len(grid) - 1 and grid[y+1][x] in d_adj:
          graph[(x, y)].add((x, y + 1))
          graph[(x, y+1)].add((x, y))
      elif current == "-":
        if x > 0 and grid[y][x-1] in l_adj:
          graph[(x, y)].add((x - 1, y))
          graph[(x-1, y)].add((x, y))
        if x < len(grid[y]) - 1 and grid[y][x+1] in r_adj:
          graph[(x, y)].add((x + 1, y))
          graph[(x+1, y)].add((x, y))
      elif current == "F":
        if y < len(grid) - 1 and grid[y+1][x] in d_adj:
          graph[(x, y)].add((x, y + 1))
          graph[(x, y+1)].add((x, y))
        if x < len(grid[y]) - 1 and grid[y][x+1] in r_adj:
          graph[(x, y)].add((x + 1, y))
          graph[(x+1, y)].add((x, y))
      elif current == "7":
        if y < len(grid) - 1 and grid[y+1][x] in d_adj:
          graph[(x, y)].add((x, y + 1))
          graph[(x, y+1)].add((x, y))
        if x > 0 and grid[y][x-1] in l_adj:
          graph[(x, y)].add((x - 1, y))
          graph[(x-1, y)].add((x, y))
      elif current == "J":
        if y > 0 and grid[y-1][x] in u_adj:
          graph[(x, y)].add((x, y - 1))
          graph[(x, y-1)].add((x, y))
        if x > 0 and grid[y][x-1] in l_adj:
          graph[(x, y)].add((x - 1, y))
          graph[(x-1, y)].add((x, y))
      elif current == "S":
        start = (x, y)
      elif current == "L":
        if y > 0 and grid[y-1][x] in u_adj:
          graph[(x, y)].add((x, y - 1))
          graph[(x, y-1)].add((x, y))
        if x < len(grid[y]) - 1 and grid[y][x+1] in r_adj:
          graph[(x, y)].add((x + 1, y))
          graph[(x+1, y)].add((x, y))
  path = get_path(graph, start)
  return path, grid

def part1(data):
  path, _ = data
  return len(path)/2

def pnpoly(nvert, vertx, verty, testx, testy):
  c = False
  for i in range(nvert):
      j = (i - 1) % nvert
      if ((verty[i] > testy) != (verty[j] > testy)) and (testx < (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i]) + vertx[i]):
          c = not c
  return c

def part2(data):
  path, grid = data

  xs, ys = zip(*path)
  path_len = len(path)
  inside = []
  for y in tqdm(range(len(grid))):
    for x in range(len(grid[y])):
      if (x, y) not in path and pnpoly(path_len, xs, ys, x, y):
        inside.append((x, y))
  return len(inside)

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))