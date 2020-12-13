import math

with open('input.txt', 'r') as file:
  inpt = [r for r in file.read().split('\n')]
  earliest_time = int(inpt[0])
  time_table = [int(b) for b in inpt[1].split(',') if b != 'x']
  closest_departures = [t * math.ceil(earliest_time / t) for t in time_table]
  
  closest = min(closest_departures)
  line_id = time_table[closest_departures.index(closest)]
  time_lost = closest - earliest_time

  print(line_id*time_lost)