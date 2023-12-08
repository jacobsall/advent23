from itertools import cycle
import numpy as np
f = open("inputs/8.txt")
data = f.read().strip()

test_data = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()

test_data2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip()

def process(data):
  instr, nodes = data.split("\n\n")
  instr = list(instr.strip())

  lines = nodes.strip().split("\n")
  things = [line.split(" = ") for line in lines]
  nodes = {n : {'L': v[1:4], 'R': v[6:9]} for n, v in things}
  return instr, nodes

def calc(graph, instr, start , stop):
  nodes = [n for n in graph if start(n)]
  results = []
  for node in nodes:
    instructions = cycle(instr)
    cur_node = node
    steps = 0
    while not stop(cur_node):
        cur_node = graph[cur_node][next(instructions)]
        steps += 1
    results.append(steps)
  return np.lcm.reduce(results)

def part1(data):
  start = lambda x: x == 'AAA'
  stop = lambda x: x == 'ZZZ'
  instr, nodes = data
  return calc(nodes, instr, start, stop)

def part2(data):
  start = lambda x: x[-1] == 'A'
  stop = lambda x: x[-1] == 'Z'
  instr, nodes = data
  return calc(nodes, instr, start, stop)
  

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))