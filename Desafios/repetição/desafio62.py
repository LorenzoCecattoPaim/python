r=int(input('Qual a razão da P.A.? '))
pri=int(input('Qual o primeiro termo da P.A.? '))
termo=pri
cont=1
mais=10
total=0
while mais!=0:
    total += mais
    while cont<=total:
        print(' {} -> '.format(termo),end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais=int(input('Quantos termos você quer que mostre a mais? '))
print('FIM DA P.A, COM {} TERMOS'.format(total))