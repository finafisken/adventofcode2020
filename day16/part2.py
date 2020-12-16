from itertools import zip_longest

def get_range(str):
  r = str.split('-')
  return range(int(r[0]), int(r[1])+1)

def get_ranges(str):
  r_strs = str.split(' or ')
  return get_range(r_strs[0]), get_range(r_strs[1])

def validate_ticket(ticket, num_to_field):
  num_check = [int(tn) in num_to_field for tn in ticket.split(',')]
  return all(num_check)

def remove_solved(fields, solved_fields):
  solved = set(field for i, field in solved_fields)
  # set subtraction, remove solved fields set from possible fields for index
  return fields - solved


with open('input.txt', 'r') as file:
  [rule_strs, myticket, tickets] = [s for s in file.read().split('\n\n')]
  myticket = myticket.replace('your ticket:\n', '').split(',')
  tickets = tickets.replace('nearby tickets:\n', '').split('\n')

  # create a dict where each number has a list of fields its valid for
  num_to_field = {}
  all_fields = set()
  for r in rule_strs.split('\n'):
    [field, ranges] = r.split(': ')
    all_fields.add(field)

    for i1, i2 in zip_longest(*get_ranges(ranges)):
      if i1 and i1 in num_to_field:
        num_to_field[i1].add(field)
      elif i1:
        num_to_field[i1] = set([field])
      if i2 and i2 in num_to_field:
        num_to_field[i2].add(field)
      elif i2:
        num_to_field[i2] = set([field])

  valid_tickets = [t for t in tickets if validate_ticket(t, num_to_field)]
  possible_fields = [all_fields.copy() for i in range(len(all_fields))]

  # assume all fields are valid for each index
  # go through each ticket and look what fields are valid for each index
  # refine the set of possible fields for each index
  for ticket in valid_tickets:
    t_nums = [int(n) for n in ticket.split(',')]
    for i, value in enumerate(t_nums):
      for field in all_fields:
        if field not in num_to_field[int(value)]:
          possible_fields[i].discard(field)

  possible_fields = [*enumerate(possible_fields)]
  solved = []
  for _ in range(len(all_fields)):
    # find fields where there is only one possiblity
    solved_fields = [(i, list(p)[0]) for i, p in possible_fields if len(p) == 1]
    solved.extend(solved_fields)
    # remove the solved fields from the remaining possible fields
    possible_fields = [(i, remove_solved(fields, solved_fields)) for i, fields in possible_fields if len(fields) > 1]

  result = 1
  for pos, field in solved:
    if 'departure' in field:
      result = result * int(myticket[pos])

  print(result)
