n=int(input('Digite um número para ver o fatorial? '))
c=n
f=1
print('Calculando {}! = '.format(n), end='')
while c>0:
    print('{}'.format(c),end='')
    print(' X 'if c > 1 else ' = ', end='')
    f= f*(c)
    c-=1
    
    
print('{}'.format(f),end='')