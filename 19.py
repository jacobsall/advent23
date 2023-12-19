from math import prod
f = open("inputs/19.txt")
data = f.read().strip()

test_data = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".strip()

def parse_rule(rule):
  split = rule.split(":")
  if len(split) == 1:
    return rule
  left, target = split
  category = left[0]
  operation = left[1]
  limit = int(left[2:])
  return (category, operation, limit, target)

def process(data):
  workflows, parts = data.split("\n\n")
  workflows = {
    wf.split("{")[0] : 
    [parse_rule(rule) for rule in wf.split("{")[1][:-1].split(",")] 
    for wf in workflows.splitlines()
    }
  parts = [{p[0] : int(p[2:])for p in part[1:-1].split(",")} for part in parts.splitlines()]
  return workflows, parts

def part1(data):
  workflows, parts = data

  operations = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
  }
  
  acc = []
  for part in parts:
    wf = "in"
    while wf in workflows:
      for rule in workflows[wf][:-1]:
        category, operation, limit, target = rule
        func = operations.get(operation)
        if func and func(part.get(category), limit):
          wf = target
          break
      else:
        wf = workflows[wf][-1]
    if wf == "A":
      acc.append(part)
  return sum([sum(part.values()) for part in acc])


def part2(data):
  workflows, _ = data
  parts = [['in', {'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000]}]]

  acc = []
  while parts:
    wf, part = parts.pop()

    if wf in workflows:
      for rule in workflows[wf][:-1]:
        category, operation, limit, target = rule
        r_min, r_max = part[category]

        new_part = part.copy()
        part[category] = [r_min, min(r_max, limit)] if operation == ">" else [max(r_min, limit), r_max]
        new_part[category] = [max(r_min, limit+1), r_max] if operation == ">" else [r_min, min(r_max, limit-1)]
        parts.append([target, new_part])
      else:
        wf = workflows[wf][-1]

    if wf == "A":
      acc.append(part) 
    elif wf != "R":
      parts.append([wf, part])

  return sum([prod([p[-1]-p[0]+1 for p in part.values()]) for part in acc])

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))