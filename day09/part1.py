from itertools import combinations

file = open('input.txt', 'r')
numbers = [int(n) for n in file.read().split('\n')]

preamble = 25
for i in range(preamble, len(numbers)):
  preamble_combos = list(combinations(numbers[i-preamble:i], 2))
  preamble_combos_sum = [a + b for (a, b) in preamble_combos]
  if i < len(numbers) and numbers[i] not in preamble_combos_sum:
    print(numbers[i])
    break