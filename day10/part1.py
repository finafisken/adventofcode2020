with open('input.txt', 'r') as file:
  adapter_pool = [int(n) for n in file.read().split('\n')]
  adapter_pool.extend([0, max(adapter_pool) + 3]) # add outlet and device as "adapters"
  adapter_pool.sort()

  one_jolts = 0
  three_jolts = 0
  for i in range(0, len(adapter_pool)-1):
    if adapter_pool[i] + 1 == adapter_pool[i+1]:
      one_jolts += 1
    elif adapter_pool[i] + 3 == adapter_pool[i+1]:
      three_jolts += 1

  print(one_jolts * three_jolts)