from itertools import combinations

file = open('input.txt', 'r')
numbers = [int(n) for n in file.read().split('\n')]

target = 776203571 # part 1 result
found = False

for start_i in range(0, len(numbers)):
  for end_i in range(start_i, len(numbers)):
    sequence = numbers[start_i:end_i]
    if sum(sequence) == target:
      print(min(sequence) + max(sequence))
      found = True
      break

  if found:
    break