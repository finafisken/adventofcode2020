bag_color_rules = {}

def bag_collection(bags):
  collection = {}
  for b in bags:
    if b != 'no other bags':
      b_str = b.replace(' bags', '').replace(' bag', '')
      color = b_str[2:]
      amount = int(b_str[:1])
      collection[color] = amount

  return collection

def search(color, searched):
  if 'shiny gold' in bag_color_rules[color]:
    return True
  else:
    for bag in bag_color_rules[color]:
      if bag not in searched:
        searched.append(bag)
        if search(bag, searched):
          return True
    return False

with open('input.txt', 'r') as file:
  rules = [r.replace('.', '').split(' bags contain ') for r in file.read().split('\n')]

  for r in rules:
    bag_color_rules[r[0]] = bag_collection(r[1].split(', '))

  count = len([c for c in bag_color_rules if search(c, [])])
  print(count)