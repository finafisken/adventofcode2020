def validate(passport):
  keys = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
  return False not in [k in passport for k in keys]

with open('input.txt', 'r') as file:
  passports = [l.replace('\n', ' ') for l in file.read().split('\n\n')]
  valid_passport_count = [validate(p) for p in passports].count(True)
  print(valid_passport_count)