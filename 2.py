import math
import numpy as np
f = open("inputs/2.txt")
data = f.read().strip()

cubes = {"green" : 13, "red" : 12, "blue" : 14}

def gen_round(text):
  res = {}
  for part in text.split(","):
    parts = part.strip().split(" ")
    for cube in cubes:
      if cube in part:
        res[cube] = int(parts[0])
  return res

def data_processing(data):
  lines = data.split("\n")
  games = [[gen_round(part.strip()) for part in line.split(":")[1].strip().split(";")] for line in lines]
  return games

def part1(games):
  def calc(idx, game):
    for roundy in game:
      for cube in roundy:
        if roundy[cube] > cubes[cube]:
          return 0
    return idx+1
  res = sum([calc(idx, game) for idx, game in enumerate(games)])
  return res

def part2(games):
  def calc(game):
    res = {}
    for roundy in game:
      for cube in roundy:
        res[cube] = max(res.get(cube, -math.inf), roundy[cube])
    return np.prod(list(res.values()))
  res = np.sum([calc(game) for game in games])
  return res

games = data_processing(data)

print("part 1:", part1(games))
print("part 2:", part2(games))


