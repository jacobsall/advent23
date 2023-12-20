from collections import defaultdict
from heapq import heappush,heappop
import math
f = open("inputs/17.txt")
data = f.read().strip()

test_data = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".strip()

test_data2 = """
111111111111
999999999991
999999999991
999999999991
999999999991
""".strip()

def process(data):
  grid = [list(map(int, line)) for line in data.split("\n") if line != ""]
  return grid

def neighbours(node, grid, part2):
  neighbours = []

  (x, y), direction, steps = node
  dx, dy = direction

  if steps < (10 if part2 else 3) and 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
    neighbours.append(((x + dx, y + dy), direction, steps+1, grid[y + dy][x + dx]))

  for dx, dy in (-dy, dx), (dy, -dx):
    if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and (not part2 or steps > 3):
      neighbours.append(((x + dx, y + dy), (dx, dy), 1, grid[y + dy][x + dx]))
  return neighbours

def shortest_path(grid, part2=False):
  visited = set()
  start, end = (0,0), (len(grid[0]) - 1, len(grid) - 1)
  start1, start2 = (start, (1,0), 0), (start, (0,1), 0)
  distances = defaultdict(lambda: math.inf, {start1: 0, start2: 0})
  queue = [(0,*start1), (0, *start2)]

  while queue:
    current_distance, current_node, direction, steps = heappop(queue)
    curr = (current_node, direction, steps)

    if current_node == end and (not part2 or steps > 3):
      return current_distance

    if curr in visited:
      continue

    visited.add(curr)
    for neighbour, new_direction, new_steps, weight in neighbours(curr, grid, part2):
      neigh = (neighbour, new_direction, new_steps)
      distance = current_distance + weight

      if distance < distances[neigh]:
        distances[neigh] = distance
        heappush(queue, (distance, *neigh))
  return -1

def part1(data):
  return shortest_path(data)

def part2(data):
  return shortest_path(data, part2=True)

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))