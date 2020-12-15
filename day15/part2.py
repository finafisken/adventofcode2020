with open('input.txt', 'r') as file:
  numbers = [int(n) for n in file.read().split(',')]
  memory = {}
  num = 0
  prev_num = None

  for i in range(30000000):
    if i < len(numbers):
      num = numbers[i]
    else: 
      if prev_num in memory:
        num = (i-1) - memory.get(prev_num)
      else:
        num = 0

    memory[prev_num] = i - 1
    prev_num = num

  print(prev_num)