from itertools import zip_longest

def get_range(str):
  r = str.split('-')
  return range(int(r[0]), int(r[1]))

def get_ranges(str):
  r_strs = str.split(' or ')
  return get_range(r_strs[0]), get_range(r_strs[1])

with open('input.txt', 'r') as file:
  [rule_strs, _, tickets] = [s for s in file.read().split('\n\n')]
  tickets = tickets.replace('nearby tickets:\n', '').split('\n')

  # create a dict where each number has a list of fields its valid for
  num_to_field = {}
  for r in rule_strs.split('\n'):
    [field, ranges] = r.split(': ')

    for i1, i2 in zip_longest(*get_ranges(ranges)):
      if i1 and i1 in num_to_field:
        num_to_field[i1].append(field)
      elif i1:
        num_to_field[i1] = [field]
      if i2 and i2 in num_to_field:
        num_to_field[i2].append(field)
      elif i2:
        num_to_field[i2] = [field]

  invalid_nums = []
  for ticket in tickets:
    t_nums = [int(tn) for tn in ticket.split(',')]
    for n in t_nums:
      if n not in num_to_field:
        invalid_nums.append(n)
  
  print(sum(invalid_nums))