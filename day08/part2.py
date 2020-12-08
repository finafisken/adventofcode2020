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

def run_sequence(instructions):
  # (index, acc, history)
  state = (0, 0, [])
  while (state[0] not in state[2] and state[0] < len(instructions)):
    state = execute(instructions[state[0]], state)
  return state

with open('input.txt', 'r') as file:
  instructions = [r for r in file.read().split('\n')]
  jump_instr_index = [idx for idx, inst in enumerate(instructions) if inst[:3] == 'jmp']
  jump_instr_index.reverse()

  for j in jump_instr_index:
    modified_instructions = instructions.copy()
    modified_instructions[j] = modified_instructions[j].replace('jmp', 'nop')
    state = run_sequence(modified_instructions)
    if (state[0] == len(instructions)):
      print(state[1])
      break