valores=[]
while True:
    v=int(input('Digite um número: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido!Não vou adicionar.')
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if r =='N':
        break
valores.sort()
print(f'Os valores adicionados são {valores}')