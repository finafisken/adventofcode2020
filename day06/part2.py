
def count_answers(group):
  grp_str = ''.join(group)
  # for unique answers in each group, count if occours as many times as members
  return len([u for u in set(grp_str) if grp_str.count(u) == len(group)])

with open('input.txt', 'r') as file:
  groups = [g.split('\n') for g in file.read().split('\n\n')]
  answer_count = sum(map(count_answers, groups))

  print(answer_count)
