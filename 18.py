from tqdm import tqdm
from typing import List, Tuple
f = open("inputs/18.txt")
data = f.read().strip()

test_data = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip()

def process(data):
  return [line.split(" ") for line in data.split("\n")]

def convert(direction):
  return { "R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1) }.get(direction, "Invalid direction")

def read_hex(s):
  return int(s[2:7], 16), convert("RDLU"[int(s[-2])])

def get_path(instr, part2=False):
  path = [(0,0)]
  for i in tqdm(instr):
    r, d = read_hex(i[2]) if part2 else (int(i[1]), convert(i[0]))
    for _ in range(r):
      current = (path[-1][0] + d[0], path[-1][1] + d[1])
      path.append(current)
  return path

def pnpoly(nvert, vertx, verty, testx, testy):
  c = False
  for i in range(nvert):
    j = (i - 1) % nvert
    if ((verty[i] > testy) != (verty[j] > testy)) and (testx < (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i]) + vertx[i]):
      c = not c
  return c

def calc_area(points, edges_len): 
  # Shoelace formula and picks theorem. much faster than part1 :P
  r = 0
  for i in tqdm(range(len(points) - 1)):
    y1, x1 = points[i]
    y2, x2 = points[i + 1]
    r += x1 * y2 - x2 * y1
  return abs(r) // 2 + edges_len // 2 + 1

def part1(data):
  path = get_path(data)
  xs, ys = zip(*path)
  path_len = len(path)
  inside = []
  for y in tqdm(range(min(ys), max(ys) + 1)):
    for x in range(min(xs), max(xs) + 1):
      if (x, y) not in path and pnpoly(path_len, xs, ys, x, y):
        inside.append((x, y))
  return len(inside) + len(path) - 1

def part2(data):
  path = get_path(data, part2=True)
  return calc_area(path, len(path))

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))