import functools
f = open("inputs/7.txt")
data = f.read().strip()

test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()

def process(data):
  lines = data.split("\n")
  return [(cards, int(bet)) for cards, bet in [line.split() for line in lines]]

def compare_cards(a_cards, a_hand, b_cards, b_hand, strengths):
  if len(a_cards) < len(b_cards):
    return 1
  elif len(a_cards) > len(b_cards):
    return -1
  else:
    if a_cards[0][1] > b_cards[0][1]:
      return 1
    elif a_cards[0][1] < b_cards[0][1]:
      return -1
    else:
      for a_card, b_card in zip(a_hand, b_hand):
        if strengths.index(a_card[0]) < strengths.index(b_card[0]):
          return 1
        elif strengths.index(a_card[0]) > strengths.index(b_card[0]):
          return -1
      return 0    

def sort_hand(hand):
  return sorted(list(set([(card, hand.count(card)) for card in hand])), key=lambda x: x[1], reverse=True)

def part1(data):
  strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

  def compare(a, b):
    a_hand, _ = a
    b_hand, _ = b
    a_cards = sort_hand(a_hand)
    b_cards = sort_hand(b_hand)
    return compare_cards(a_cards, a_hand, b_cards, b_hand, strengths)
  
  sorted_l = sorted(data, key=functools.cmp_to_key(compare))
  return sum([bet * (idx + 1) for idx, (_, bet) in enumerate(sorted_l)])

def part2(data):
  strengths = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

  def apply_jokers(cards):
    if len(cards) > 1:
      for card, count in cards:
        if card == 'J':
          cards.remove((card, count))
          cards[0] = (cards[0][0], cards[0][1] + count)
          break

  def compare(a, b):
    a_hand, _ = a
    b_hand, _ = b
    a_cards = sort_hand(a_hand)
    b_cards = sort_hand(b_hand)
    apply_jokers(a_cards)
    apply_jokers(b_cards)
    return compare_cards(a_cards, a_hand, b_cards, b_hand, strengths)

  sorted_l = sorted(data, key=functools.cmp_to_key(compare))
  return sum([bet * (idx + 1) for idx, (_, bet) in enumerate(sorted_l)])

processed = process(data)
print("part 1", part1(processed))
print("part 2", part2(processed))