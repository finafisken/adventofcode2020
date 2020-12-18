import re

def get_sum(string):
  numbers = [int(n) for n in string.replace('*', '+').split('+')]
  operators = re.findall(r'\+|\*', string)
  total = numbers[0]
  for i, op in enumerate(operators):
    if op == '+':
      total += numbers[i+1]
    elif op == '*':
      total *= numbers[i+1]
  
  return total

def solve_partial(string):
  # get first closing parens
  end_i = string.find(')')
  # get last opening parens in substring of original up to first closing
  start_i = string[:end_i].rfind('(')
  # solve string[start_i+1:end_i]
  p_sum = get_sum(string[start_i+1:end_i])

  return string[:start_i] + str(p_sum) + string[end_i+1:]


with open('input.txt', 'r') as file:
  lines = [l.replace(' ', '') for l in file.read().split('\n')]

  sums = []
  for line in lines:
    for p in range(line.count('(')):
      line = solve_partial(line)

    sums.append(get_sum(line))

  print(sum(sums))