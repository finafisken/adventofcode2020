with open('input.txt', 'r') as file:
  groups = [f.replace('\n', '') for f in file.read().split('\n\n')]
  group_count = [len(set(*g.split())) for g in groups]
  print(sum(group_count))