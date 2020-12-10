def paths_from_adapter(i, adapter_pool, memo):
  # by storing possible paths for each adapter we only need to run it once
  if i in memo:
    return memo[i]

  # last step will only have one possible path
  if i == len(adapter_pool)-1:
    return 1

  total_paths = 0

  # look through remaining adapters that are within 3 jolts
  for j in range(i+1, len(adapter_pool)):
    if adapter_pool[j] - adapter_pool[i] > 3:
      break

    # call recursively until we hit last-1 adapter, save result to memo and add to total count
    memo[j] = paths_from_adapter(j, adapter_pool, memo)
    total_paths += memo[j]

  return total_paths

with open('input.txt', 'r') as file:
  adapter_pool = [int(n) for n in file.read().split('\n')]
  adapter_pool.extend([0, max(adapter_pool)+ 3]) # add outlet and device as "adapters"
  adapter_pool.sort()

  total_paths = paths_from_adapter(0, adapter_pool, {})
  print(total_paths)