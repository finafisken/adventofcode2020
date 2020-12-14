def mask_val(mask, bin_val):
  val = ''
  for i, c in enumerate(mask):
    if c == 'X':
      val += bin_val[i]
    elif c == '0':
      val += '0'
    elif c == '1':
      val += '1'

  return val

with open('input.txt', 'r') as file:
  lines = [l for l in file.read().split('\n')]
  
  mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  mem = {}
  for line in lines:
    if 'mask' in line:
      mask = line[7:]
    else:
      [pos, val] = line.split(' = ')
      bin_val = format(int(val), '036b') # convert to binary with 36 chars, fill empty with 0
      masked_val = mask_val(mask, bin_val)
      mem_pos = pos[4:-1]
      mem[mem_pos] = masked_val

  dec_values = [int(v, 2) for v in mem.values()]

  print(sum(dec_values))