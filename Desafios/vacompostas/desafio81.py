valores=[]
c=0
while True:
    v=int(input('Digite um número: '))
    valores.append(v)
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if r =='N':
        break
    c+=1
print(f'Foram digitados {c} valores')
valores.sort(reverse=True)
print(f'A lista do maior para o menor é {valores}')
if 5 not in valores:
    print('O valor 5 não foi adicionado.')
else:
    print('O valor 5 foi adicionado!')