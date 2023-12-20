from math import prod
f = open("inputs/20.txt")
data = f.read().strip()

test_data = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""".strip()

test_data2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""".strip()

def process(data):
  pulsers = {}
  flippers = {}
  conjunctions = {}
  for line in data.split("\n"):
    left, right = line.split(" -> ")
    if left.startswith("%"):
      flippers[left[1:]] = 0
      pulsers[left[1:]] = right.split(", ")
    elif left.startswith("&"):
      conjunctions[left[1:]] = {}
      pulsers[left[1:]] = right.split(", ")
    else:
      pulsers[left] = right.split(", ")

  for line in data.split("\n"):
    left, right = line.split(" -> ")
    if left.startswith("%") or left.startswith("&"):
      left = left[1:]
    for d in right.split(", "):
      if d in conjunctions:
        conjunctions[d][left] = 0
  return pulsers, flippers, conjunctions

def part1(data):
  pulsers, flipflops, conjunctions = data

  pulses = [0, 0]
  for _ in range(1000):
    pulseQueue = []
    pulseQueue.append(("button", "broadcaster", 0))
    while pulseQueue:
      source, target, pulse = pulseQueue.pop(0)
      pulses[pulse] += 1

      if target == "broadcaster":
        for t in pulsers[target]:
          pulseQueue.append((target, t, pulse))
      elif target in flipflops:
        if not pulse:
          flipflops[target] = 1 - flipflops[target]
          next_pulse = flipflops[target]
        else:
          continue
        for t in pulsers[target]:
          pulseQueue.append((target, t, next_pulse))
      elif target in conjunctions:
        conjunctions[target][source] = pulse
        new_pulse = not all(conjunctions[target].values())
        for t in pulsers[target]:
          pulseQueue.append((target, t, new_pulse))
  return prod(pulses)

def part2(data):
  return "TODO"

processed = process(data)
print("part 1:", part1(processed))
print("part 2:", part2(processed))