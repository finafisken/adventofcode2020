import math

def half(d, min, max):
  if d:
    # lower half
    return (min, math.floor((max-min) / 2 + min))
  else:
    # upper half
    return (math.floor((max-min) / 2 + min), max)

def get_row(instr):
  row_instruction = instr[:7]
  max_row = 127
  min_row = 0

  for dir in row_instruction:
    (min_row, max_row) = half(dir == 'F', min_row, max_row)
  
  return max_row

def get_col(instr):
  col_instruction = instr[7:]
  max_col = 7
  min_col = 0

  for dir in col_instruction:
    (min_col, max_col) = half(dir == 'L', min_col, max_col)
  
  return max_col

with open('input.txt', 'r') as file:
  seat_instructions = [l for l in file.read().split('\n')]
  seat_ids = [get_row(s) * 8 + get_col(s) for s in seat_instructions]
  possible_seat_ids = [r * 8 + c for r in range(0, 127) for c in range(0, 7) if r * 8 + c not in seat_ids]

  for id in possible_seat_ids:
    if id+1 in seat_ids and id-1 in seat_ids:
      print(id)