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
  index = 0
  accumulator = 0
  history = []
  while (index not in history and index < len(instructions)):
    index, accumulator, history = execute(instructions[index], (index, accumulator, history))
  return (index, accumulator, history)

with open('input.txt', 'r') as file:
  instructions = [r for r in file.read().split('\n')]
  jump_instr_index = [idx for idx, inst in enumerate(instructions) if inst[:3] == 'jmp']
  jump_instr_index.reverse()

  for j in jump_instr_index:
    modified_instructions = instructions.copy()
    modified_instructions[j] = modified_instructions[j].replace('jmp', 'nop')
    index, accumulator, _ = run_sequence(modified_instructions)
    if (index == len(instructions)):
      print(accumulator)
      break