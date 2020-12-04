import math

def validate_number(num, min = 0, max = math.inf, length = None):
  try: 
    n = int(num)
    if length and len(num) != length:
      return False
    return n >= min and n <= max
  except:
    return False

def validate_ecl(ecl):
  valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  return ecl in valid_colors

def validate_hcl(hcl):
  hex = hcl.replace('#', '0x')

  if len(hex) != 8: return False

  try:
    int(hex, 16)
    return True
  except:
    return False

def validate_hgt(hgt):
  unit = hgt[-2:]
  n = hgt[:-2]

  if unit == 'cm':
    return validate_number(n, 150, 193)
  if unit == 'in':
    return validate_number(n, 59, 76)
  
  return False


def validate(passport):
  valid = True
  validators = {
    'byr:': lambda n: validate_number(n, 1920, 2002, 4),
    'iyr:': lambda n: validate_number(n, 2010, 2020, 4),
    'eyr:': lambda n: validate_number(n, 2020, 2030, 4),
    'hgt:': validate_hgt,
    'hcl:': validate_hcl,
    'ecl:': validate_ecl,
    'pid:': lambda n: validate_number(n, 0, math.inf, 9),
  }

  split_passport = passport.split(' ')

  for key in validators.keys():
    if key not in passport:
      return False

  for part in split_passport:
    key = part[:4]
    if key not in validators.keys(): continue
    value = part [4:]
    valid = validators[key](value)

    if not valid:
      break

  return valid



with open('input.txt', 'r') as file:
  passports = map(lambda l: l.replace('\n', ' '), file.read().split('\n\n'))
  valid_passports = list(filter(lambda p: validate(p), passports))
  print(len(valid_passports))