import numpy as np
f = open("inputs/3.txt")
data = f.read().strip()

def process(data):
  directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

  def evaluate(text):
    try:
      int(text)
      return False
    except ValueError:
      return text != "."

  lines = data.split("\n")
  things = [list(line) for line in lines]
  res = {}

  for i in range(len(things)):
    current = ""
    symbols = set()
    done = False
    for j in range(len(things[i])):
      try:
        int(things[i][j])
        current += things[i][j]

        for direction in directions:
          try:
            new_i = i + direction[0]
            new_j = j + direction[1]
            symbol = things[new_i][new_j]
            if evaluate(symbol):
              symbols.add((new_i, new_j, symbol))
          except IndexError:
            pass
      except ValueError:
        done = True

      if j == len(things[i])-1 or done:
        if current != "" and len(symbols) > 0:
          for symbol in symbols:
            try:
              res[symbol].append((i,j,int(current)))
            except KeyError:
              res[symbol] = [(i,j,int(current))]
        current = ""
        done = False
        symbols = set()
  return res

def part1(data):
  return sum([x[2] for v in data.values() for x in v])

def part2(data):
  for key in data:
    if len(data[key]) > 1 and key[2] == "*":
      data[key] = np.prod([part[2] for part in data[key]])
    else:
      data[key] = 0
  return sum(data.values())

processed = process(data)

print("part 1:", part1(processed))
print("part 2:", part2(processed))



