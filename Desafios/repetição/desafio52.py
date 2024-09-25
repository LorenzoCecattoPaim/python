n=int(input('Digite um número: '))
tot=0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('O número é foi divido {} vezes'.format(tot))
if tot==2:
    print('O número {} é primo, pois só tem 2 divisores'.format(n))
else:
    print('NÃO é primo!')