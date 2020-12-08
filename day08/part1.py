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

  # (index, acc, history)
  state = (0, 0, [])
  while (state[0] not in state[2]):
    state = execute(instructions[state[0]], state)
  
  print(state[1])