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
  pos1 = item['password'][item['min']-1] == item['char']
  pos2 = item['password'][item['max']-1] == item['char']
  return pos1 != pos2

with open('input.txt', 'r') as file:
  data = map(parse_line, file.read().splitlines())
  valid_pws = list(filter(validate, data))
  print(len(valid_pws))
