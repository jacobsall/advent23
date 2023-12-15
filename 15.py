f = open("inputs/15.txt")
data = f.read().strip()

test_data = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip()

def process(data):
  return data.split(",")

def hash(part):
  value = 0
  for char in part:
    value = (value + ord(char)) * 17 % 256
  return value

def part1(data):
  return sum([hash(part) for part in data])

def part2(data):
  hmap = {}
  boxes = {i:[] for i in range(256)}
  for part in data:
    if '=' in part:
      label, num = part.split("=")
      num = int(num)
      box = hash(label)
      if label not in hmap:
        hmap[label] = len(boxes[box])
        boxes[box].append([label, num])
      else:
        boxes[box][hmap[label]][1] = num
    else:
      label, num = part.split("-")
      box = hash(label)
      if label in hmap:
        boxes[box].pop(hmap[label])
        if len(boxes[box]) > 0: 
          for i in range(hmap[label],len(boxes[box])):
            hmap[boxes[box][i][0]] -= 1
        del hmap[label]
  return sum([sum([(box+1) * (l_idx+1) * lens[1] for l_idx,lens in enumerate(boxes[box])]) for box in boxes])

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))