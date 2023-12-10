import operator
f = open("inputs/9.txt")
data = f.read().strip()

test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()

def process(data):
  lines = data.split("\n")
  numbers = [[int(n) for n in line.split(" ")] for line in lines]
  return numbers

def calc(data, func):
  result = [] 
  for row in data:
    new_rows = [row]
    while min(new_rows[-1]) < 0 or max(new_rows[-1]) > 0:
      new_rows.append(list(map(operator.sub, new_rows[-1][1:], new_rows[-1][:-1])))
    result.append(func(new_rows))
  return sum(result)

def part1(data):
  def func(new_rows):
    last_value = 0
    for row in reversed(new_rows):
      row.append(row[-1] + last_value)
      last_value = row[-1]
    return last_value
  return calc(data, func)

def part2(data):
  def func(new_rows):
    last_value = 0
    for row in reversed(new_rows):
      row.insert(0, row[0] - last_value)
      last_value = row[0]
    return last_value
  return calc(data, func)

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))