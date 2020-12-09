with open('input.txt', 'r') as file:
  numbers = [int(n) for n in file.read().split('\n')]

  target = 776203571 # part 1 result
  found = False

  for start_i in range(0, len(numbers)):
    for end_i in range(start_i, len(numbers)):
      sequence = numbers[start_i:end_i]
      total = sum(sequence)

      if total > target:
        break
      if total == target:
        print(min(sequence) + max(sequence))
        found = True
        break

    if found:
      break