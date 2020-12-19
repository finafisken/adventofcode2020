def validate(string, order, rules):
  if len(order) > len(string):
    return False
  elif len(order) == 0 or len(string) == 0:
    return len(order) == len(string)

  c = order.pop()
  if c == 'a' or c == 'b':
    if string[0] == c:
      return validate(string[1:], order.copy(), rules)
  else:
    for rule in rules[c]:
      if validate(string, order + list(reversed(rule)), rules):
        return True
  return False

with open('input.txt', 'r') as file:
  r_list, messages = [l.split('\n') for l in file.read().split('\n\n')]

  rules = {}
  for r in r_list:
    key, val = r.split(': ')
    if '"' in val:
      rules[key] = val.replace('"', '')
    else:
      rules[key] = [v.split() for v in val.split(' | ')]

  rules['8'] = [['42'], ['42', '8']]
  rules['11'] = [['42', '31'], ['42', '11', '31']]

  rule_zero = rules['0'][0]
  valid_count = [validate(m, list(reversed(rule_zero)), rules) for m in messages].count(True)

  print(valid_count)