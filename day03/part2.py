import math

def check_path(step_x, step_y):
  with open('input.txt', 'r') as file:
    x = 0
    count = 0
    for y, line in enumerate(file.readlines()):
      # skip lines according to step_y
      if y == 0 or y % step_y != 0:
        continue

      # looping index, strip \n char from line
      x = (x + step_x) % len(line.strip())
      # cast bool as int before increment
      count += int(line[x] == '#')

    return count

path_steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_on_paths = map(lambda steps: check_path(*steps), path_steps)

print(math.prod(trees_on_paths))
