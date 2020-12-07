def bag_collection(bags):
  collection = []
  for b in bags:
    color = None
    amount = 0
    if b != 'no other bags':
      b_str = b.replace(' bags', '').replace(' bag', '')
      color = b_str[2:]
      amount = int(b_str[:1])
    collection.append((color, amount))
  return collection

def search(content, bags):
  # content = [('bright cyan', 2), ('dotted coral', 5), ('pale salmon', 5)]
  # bags = { 'dim magenta': [('dark maroon', 1), ('dull olive', 3), ('dim tomato', 5), ('wavy gold', 5)], ... }
  for (color, amount) in content:
    if color == 'shiny gold':
      # print (content)
      # print('Found')
      return True
    if color == None:
      return False
    else:
      search(bags[color], bags)

with open('input.txt', 'r') as file:
  rules = [r.replace('.', '').split(' bags contain ') for r in file.read().split('\n')]
  bag_color_rules = {}
  for r in rules:
    bag_color_rules[r[0]] = bag_collection(r[1].split(', '))
  print(bag_color_rules)
  count = 0
  for color, content in bag_color_rules.items():
    # print(color, content)
    if search(content, bag_color_rules):
      count += 1
    # print(search(content, bag_color_rules))
  print(count)