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

print(check_path(3,1))