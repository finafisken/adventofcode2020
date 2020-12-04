keys = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

def validate(passport):
  valid = True
  for key in keys:
    if key in passport:
      continue
    else:
      valid = False
      break
  return valid

with open('input.txt', 'r') as file:
  passports = map(lambda l: l.replace('\n', ' '), file.read().split('\n\n'))
  valid_passports = filter(lambda p: validate(p), passports)
  print(len(list(valid_passports)))