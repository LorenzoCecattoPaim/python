r=int(input('Qual a razão da P.A.? '))
pri=int(input('Qual o primeiro termo da P.A.? '))
termo=pri
cont=1
while cont<=10:
    print(' {} ->'.format(termo),end='')
    termo+=r
    cont+=1
print('FIM')
