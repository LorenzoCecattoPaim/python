n1=float(input('Qual é a sua primeira nota? '))
n2=float(input('Qual é a sua segunda nota? '))
media=(n1+n2)/2
if media < 5:
    print('Você está REPROVADO!')
elif media >=5 and media <6.9:
    print('Você está de RECUPERAÇÃO!')
elif media >=7:
    print('Você está APROVADO!!!')