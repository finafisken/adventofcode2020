bag_color_rules = {}

def bag_collection(bags):
  collection = {}
  for b in bags:
    color = None
    amount = 0
    if b != 'no other bags':
      b_str = b.replace(' bags', '').replace(' bag', '')
      color = b_str[2:]
      amount = int(b_str[:1])
    collection[color] = amount
  return collection

def count_bags(color):
  count = 0
  if len(bag_color_rules[color]):
    for bag in bag_color_rules[color]:
      if not bag:
        continue
      count += bag_color_rules[color][bag] + (bag_color_rules[color][bag] * count_bags(bag))
    return count
  else:
    return 0

with open('input.txt', 'r') as file:
  rules = [r.replace('.', '').split(' bags contain ') for r in file.read().split('\n')]
  
  for r in rules:
    bag_color_rules[r[0]] = bag_collection(r[1].split(', '))

  print(count_bags('shiny gold'))