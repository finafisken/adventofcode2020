with open('input.txt', 'r') as file:
  lines = [r for r in file.read().split('\n')]
  index_and_bus = [(i, int(b)) for i, b in enumerate(lines[1].split(',')) if b != 'x']

  step = index_and_bus[0][1]
  t = step

  for index, bus in index_and_bus[1:]:
    while (t + index) % bus != 0:
      t += step
    step = step * bus

  print(t)