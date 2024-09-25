pessoa={}
cópia=[]
mulher=[]
idade=[]
acme=[]
média=0
tot=0
while True:
    pessoa['nome']=input('Nome:')
    pessoa['sexo']=input('Sexo:[M/F] ').upper()
    pessoa['idade']=int(input('Idade: '))
    idade.append(pessoa['idade'])
    cópia.append(pessoa.copy())
    if pessoa['sexo']=='F':
        mulher.append(pessoa['nome'])
    tot+=1
    média=((sum(idade))/tot)

    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if r=='N':
        break
print('=-'*20)
print(f'- O grupo tem {tot} pessoas.')
print(f'- A média de idade é de {média:.2f} anos.')
print(f'As mulheres cadastradas: {mulher}')
print(f'- Lista de pessoas que estão acima da média:')
for p in cópia:
    if p['idade'] >= média:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v}: ',end='')
            print()
print('FIM DO PROGRAMA')
