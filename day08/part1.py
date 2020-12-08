def execute(instruction, state):
  (index, accumulator, history) = state
  op = instruction[:3]
  arg = int(instruction[4:])
  history.append(index)

  if op == 'acc':
    accumulator += arg
    index += 1
  elif op == 'jmp':
    index += arg
  else:
    index += 1

  return (index, accumulator, history)


with open('input.txt', 'r') as file:
  instructions = [r for r in file.read().split('\n')]

  index = 0
  accumulator = 0
  history = []

  while (index not in history and index < len(instructions)):
    index, accumulator, history = execute(instructions[index], (index, accumulator, history))
  
  print(accumulator)