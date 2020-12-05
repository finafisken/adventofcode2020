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
  # print(f'row min:{min_row}, row max:{max_row}')

def get_col(instr):
  col_instruction = instr[7:]
  max_col = 7
  min_col = 0

  for dir in col_instruction:
    (min_col, max_col) = half(dir == 'L', min_col, max_col)
  
  return max_col
  # print(f'col min:{min_col}, col max:{max_col}')


with open('input.txt', 'r') as file:
  seat_instructions = [l for l in file.read().split('\n')]
  max_seat_id = max([get_row(s) * 8 + get_col(s) for s in seat_instructions])
  print(max_seat_id)