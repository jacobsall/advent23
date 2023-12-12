import functools
from tqdm import tqdm
f = open("inputs/12.txt")
data = f.read().strip()

test_data = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()

def process(data):
  lines = data.split("\n")
  return [(line.split(" ")[0], tuple([int(num) for num in line.split(" ")[1].split(",")]) )for line in lines]

def check_counts(pattern, counts):
    start = 0
    for count in counts:
        # Find the next group of '#'
        start = pattern.find('#', start)
        if start == -1:
            return False
        end = pattern.find('.', start)
        if end == -1:
            end = len(pattern)
        # Check if the count matches
        if end - start != count:
            return False
        start = end
    # Check if there are any extra '#' in the pattern
    if '#' in pattern[start:]:
        return False
    return True

def brute_force(pattern, counts):
  replaced = pattern.replace('?', '.')
  if check_counts(replaced, counts):
    return 1
  elif '?' not in pattern:
    return 0
  else:
    q_idx = pattern.index('?')
    return brute_force(pattern[:q_idx] + "#" + pattern[q_idx+1:], counts) + brute_force(pattern[:q_idx] + "." + pattern[q_idx+1:], counts) 

@functools.cache
def dp(pattern, counts):

  if pattern == '':
    if len(counts) == 0:
      return 1 # No remaining characters, and no remaining counts
    return 0 # No remaining characters, but there are remaining counts that can't be satisfied
  
  if len(counts) == 0:
    if '#' not in pattern:
      return 1 # All the remaining characters are '.' or '?'
    return 0 # There are remaining '#' but no remaining counts, they've been spent too early
  
  if pattern[0] == '.':
    return dp(pattern[1:], counts) # it's a dot, just look forward
  if pattern[0] == '?':
    return dp('#' + pattern[1:], counts) + dp('.' + pattern[1:], counts) # two paths open, replace '?' with '#' or '.'
  elif pattern[0] == '#':
    if len(pattern) < counts[0]:
      return 0 # there's not enough space in the pattern for the count
    elif '.' in pattern[:counts[0]]:
      return 0 # there's a '.' in the way of the count
    elif len(pattern) > counts[0] and pattern[counts[0]] == '#':
      return 0 # there's a '#' after the count, each count must be followed by a '.'
    else:
      return dp(pattern[counts[0]+1:], counts[1:]) # the count fit, look forward with the remaining counts


def part1(data):
  results = []
  for pattern, counts in tqdm(data):
    results.append(brute_force(pattern, counts)) # brute force all the possible patterns
  return sum(results)

def part2(data):
  results = []
  for pattern, counts in tqdm(data):
    results.append(dp((pattern + '?')*4 + pattern, counts*5))
  return sum(results)

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))