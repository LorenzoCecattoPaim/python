
tot=0
soma=0
n=0
while n != 999:
    n=int(input('Digite algum número[Parar digite 999]: '))
    tot+=1
    soma+=n
print('FIM')
print('Ao total  foram {} números'.format(tot-1))
print('E a soma de todos eles é {}'.format(soma-999))