menor=0
maior=0
for p in range(1,6):
    peso=float(input('Qual o peso da {}º pesssoa? '.format(p)))
    if p==1:
        menor=peso
        maior=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print('O menor peso é {}'.format(menor))
print('O maior peso é {}'.format(maior))