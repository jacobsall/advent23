import re
import numpy as np
f = open("inputs/4.txt")
data = f.read().strip()

test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()

def process(data):
  return [[re.split('\\s+', numbers.strip()) for numbers in line.split(":")[1].split("|")] for line in data.split("\n")] 

def part1(cards):
  def score(card):
    matches = len(np.intersect1d(card[0], card[1]))
    return pow(2, matches-1) if matches > 1 else matches

  return sum([score(card) for card in cards])

def part2(cards):
  copies = np.ones(len(cards))
  for idx, card in enumerate(cards):
    matches = len(np.intersect1d(card[0], card[1]))
    for i in range(matches):
      copies[idx+i+1] += int(copies[idx])
  return int(sum(copies))

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))