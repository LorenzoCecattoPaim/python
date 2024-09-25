print('-'*20)
print('PRODUTOS CADASTRADOS')
print('-'*20)
menor=0
caro=s=tot=0
barato=''
while True:
    n=input('Qual o nome do produto? ')
    p=float(input('Quanto custa este produto? R$'))
    r=input('Quer continuar adicionando produtos?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar adicionando produtos?[S/N] ').upper()
    s += p
    tot=+1
    if tot==1:
        menor=p
        barato=n
    else:
        if p<menor:
            menor=p
            barato=n
    if p > 1000:
        caro+=1
    if r == 'N':
        break
print(f'O total gasto foi {s} reais, com {caro} produtos custando mais de 1000 reais')
print(f'O produto mais barato é o {barato} e custa {menor}')