def move(dir, distance, pos):
  (x, y) = pos
  if dir == 'N':
    y += distance
  elif dir == 'S':
    y -= distance
  elif dir == 'E':
    x += distance
  elif dir == 'W':
    x -= distance

  return (x, y)

def turn(facing, turn_dir, deg):
  deg = deg * -1 if turn_dir == 'L' else deg
  norm_deg = deg % 360

  new_face = {
    'N': {
      90: 'E',
      180: 'S',
      270: 'W',
    },
    'S': {
      90: 'W',
      180: 'N',
      270: 'E',
    },
    'E': {
      90: 'S',
      180: 'W',
      270: 'N',
    },
    'W': {
      90: 'N',
      180: 'E',
      270: 'S',
    }
  }

  return new_face[facing][norm_deg]


with open('input.txt', 'r') as file:
  nav_instructions = [r for r in file.read().split('\n')]

  facing = 'E'
  pos = (0,0)

  for inst in nav_instructions:
    action = inst[:1]
    distance = int(inst[1:])

    if action == 'F':
      pos = move(facing, distance, pos)
    elif action in 'LR':
      facing = turn(facing, action, distance)
    else:
      pos = move(action, distance, pos)

  manhattan_dist = abs(pos[0])+abs(pos[1])
  print(manhattan_dist)
