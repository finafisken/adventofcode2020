from math import sin, cos, radians

def move_wp(dir, distance, pos):
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

def rotate_wp(turn_dir, deg, waypoint):
  deg = deg * -1 if turn_dir == 'R' else deg
  rad = radians(deg)

  (x,y) = waypoint
  
  # vector rotation
  rx = round(x*cos(rad) - y*sin(rad))
  ry = round(x*sin(rad) + y*cos(rad))

  return (rx, ry)

def move(pos, waypoint, distance):
  (x, y) = pos
  (wx, wy) = waypoint

  return (x + distance * wx, y + distance * wy)

with open('input.txt', 'r') as file:
  nav_instructions = [r for r in file.read().split('\n')]

  pos = (0,0)
  waypoint = (10, 1)

  for inst in nav_instructions:
    action = inst[:1]
    distance = int(inst[1:])
    
    if action == 'F':
      pos = move(pos, waypoint, distance)
    elif action in 'LR':
      waypoint = rotate_wp(action, distance, waypoint)
    else:
      waypoint = move_wp(action, distance, waypoint)

  manhattan_dist = abs(pos[0])+abs(pos[1])
  print(manhattan_dist)