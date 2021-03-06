from collections import defaultdict
from itertools import product

def get_neighbor_coords(pos):
  x,y,z,w = pos
  deltas = product([-1, 0, 1], repeat=4)
  neighbors = [(x+dx, y+dy, z+dz, w+dw) for dx, dy, dz, dw in deltas if (dx,dy,dz,dw) != (0,0,0,0)]

  return neighbors

with open('input.txt', 'r') as file:
  rows = [r for r in file.read().split('\n')]
  cube_at_pos = defaultdict(lambda:'.')

  for y, r in enumerate(rows):
    for x, c in enumerate(r):
      cube_at_pos[(x,y,0, 0)] = c

  for cycle in range(6):
    next_cube_at_pos = defaultdict(lambda:'.')
    all_neighbors = set()

    for pos in cube_at_pos.keys():
      all_neighbors.update(get_neighbor_coords(pos))

    for p in all_neighbors:
      neighbors = get_neighbor_coords(p)
      active_neighbors = sum(int(cube_at_pos[n] == '#') for n in neighbors)
      # active -> active if active_neighbors 2 or 3
      if cube_at_pos[p] == '#' and (1 < active_neighbors < 4):
        next_cube_at_pos[p] = '#'
      # inactive -> active if active_neighbors 3
      elif cube_at_pos[p] == '.' and active_neighbors == 3:
        next_cube_at_pos[p] = '#'

    cube_at_pos = next_cube_at_pos

  count_list = [int(c == '#') for c in cube_at_pos.values()]
  print(sum(count_list))