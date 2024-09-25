galera=[]
dado=[]
pesadas=[]
leves=[]
tot=0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    tot+=1
    for p in galera:
        if p[1] >= 100:
            pesadas.append(p[0][:])
            maior=p[1]
        elif p[1]<=75:
            leves.append(p[0][:])
            menor=p[1]
    dado.clear()
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if r =='N':
        break
print(galera)
print('-_='*20)
print(f'Você cadastrou {tot} pessoas!')
print(f'O maior peso foi de {maior}. Peso de {pesadas[:]}')
print(f'O menor peso foi de {menor}. Peso de {leves[:]}')
