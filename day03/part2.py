import math

def check_path(step_x, step_y):
  with open('input.txt', 'r') as file:
    x = 0
    count = 0
    for y, line in enumerate(file.readlines()):
      if y == 0 or y % step_y != 0:
        continue

      line = line.strip()
      max_x = len(line)
      n_x = x + step_x

      x = n_x if n_x < max_x else n_x - max_x

      if line[x] == '#':
        count += 1

    return count

path_steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_on_paths = map(lambda steps: check_path(*steps), path_steps)

print(math.prod(trees_on_paths))
