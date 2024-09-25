mediaidade=0
somaidade=0
maioridadadah=0
velhonome=0
totmulher=0
for p in range(1,5):
    print('--------{}º PESSOA--------'.format(p))
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=input('Sexo[M/F]: ')
    somaidade+=idade
    if p == 1 and sexo in 'Mm':
        maioridadadah=idade
        velhonome=nome
    else:
        if sexo in 'Mm' and maioridadadah<idade:
            maioridadadah=idade
            velhonome=nome
    if sexo in 'Ff' and idade<20:
        totmulher+=1
mediaidade=somaidade/4
print('A média das idades é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadadah,velhonome))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher))
