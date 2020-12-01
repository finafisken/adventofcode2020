numbers = open('./input.txt', 'r').read().split('\n')
numbers = [int(i) for i in numbers]

for n in numbers:
    x = 2020 - n
    if x in numbers:
        print('n: {}, x: {}, x*n: {}'.format(x, n, x*n))
        break
