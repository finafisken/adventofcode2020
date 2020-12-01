numbers = open('./input.txt', 'r').read().split('\n')
numbers = [int(i) for i in numbers]

found = False
for n1 in numbers:
    for n2 in numbers:
        n3 = 2020 - n1 - n2
        if n3 in numbers:
            found = True
            print('n1: {}, n2: {}, n3: {}, n1*n2*n3: {}'.format(n1, n2, n3, n1*n2*n3))
            break
    if found:
        break
