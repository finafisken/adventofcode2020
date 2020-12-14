def mask_val(mask, binary):
  masked = ''
  for i, c in enumerate(mask):
    if c == 'X':
      masked += 'X'
    elif c == '0':
      masked += binary[i]
    elif c == '1':
      masked += '1'

  return masked

def generate_addr(mask):
  addr_list = [mask]
  x_indexes = [i for i, c in enumerate(mask) if c == 'X']

  # for each X duplicate items in list
  # replace half X at current X-index with 0, rest with 1
  for i in x_indexes:
    ones = [addr[:i] + '1' + addr[i+1:] for addr in addr_list]
    zeros = [addr[:i] + '0' + addr[i+1:] for addr in addr_list]
    ones.extend(zeros)
    addr_list = ones

  return addr_list

with open('input.txt', 'r') as file:
  lines = [l for l in file.read().split('\n')]

  mask = '000000000000000000000000000000000000'
  mem = {}
  for line in lines:
    if 'mask' in line:
      mask = line[7:]
    else:
      [pos, val] = line.split(' = ')
      mem_pos = format(int(pos[4:-1]), '036b') # convert to binary with 36 chars, fill empty with 0
      masked_mem_pos = mask_val(mask, mem_pos)
      for pos in generate_addr(masked_mem_pos):
        mem[pos] = val

  values = [int(v) for v in mem.values()]

  print(sum(values))