f = open("inputs/1.txt")
data = f.read()

lines = data.split("\n")

letternumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum1 = 0
sum2 = 0
for line in lines:
  numbers1 = ""
  numbers2 = ""
  letters = ""
  for c in line:
    try:
      int(c)
      numbers1 += c
      numbers2 += c
    except ValueError:
      letters += c
      for l in letternumbers:
        if  l in letters:
          adding = str(letternumbers.index(l) + 1)
          numbers2 += adding
          letters = letters[-1]
  try:
    int(numbers1)
    if (len(numbers1) == 0):
      continue
    sum1 += int(numbers1[0] + numbers1[-1])
  except ValueError:
    pass

  try:
    int(numbers2)
    if (len(numbers2) == 0):
      continue
    sum2 += int(numbers2[0] + numbers2[-1])
  except ValueError:
    pass

print("part1: ", sum1, " part2: ", sum2)