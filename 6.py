from tqdm import tqdm
f = open("inputs/6.txt")
data = f.read().strip()

test_data = """
Time:      7  15   30
Distance:  9  40  200
""".strip()

def process(data):
  lines = data.split("\n")
  return [[x for x in line.split(":")[1].strip().split()] for line in lines]

def calc(time, distance):
  res = 0
  for speed in tqdm(range(time)):
    result = speed * (time - speed)
    if result > distance:
      res += 1
  return res

def part1(data):
  times, distances = [[int(value) for value in line] for line in data]
  answer = 1
  for time, dist in zip(times,distances):
    answer *= calc(time, dist)
  return answer

def part2(data):
  time, distance = [int("".join(line)) for line in data]
  return calc(time, distance)

processed = process(data)

print("part 1", part1(processed))
print("part 2", part2(processed))