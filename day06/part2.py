
with open('input.txt', 'r') as file:
  groups = [g.split('\n') for g in file.read().split('\n\n')]
  count = 0

  for g in groups:
    grp_answers_str = ''.join(g)
    unique = set(grp_answers_str)
    count += len([u for u in unique if grp_answers_str.count(u) == len(g)])

  print(count)
