def parse_line(line):
  split_line = line.split(' ')
  [min, max] = split_line[0].split('-')

  return {
    'min': int(min),
    'max': int(max),
    'char': split_line[1][:1],
    'password': split_line[2],
  }

def validate(item):
  char_count = item['password'].count(item['char'])
  return char_count >= item['min'] and char_count <= item['max']

with open('input.txt', 'r') as file:
  data = map(parse_line, file.read().splitlines())
  valid_pws = list(filter(validate, data))
  print(len(valid_pws))
