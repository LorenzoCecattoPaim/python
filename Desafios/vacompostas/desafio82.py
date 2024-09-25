valores=[]
par=[]
impar=[]
while True:
    v=int(input('Digite um número: '))
    valores.append(v)
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()

    if v % 2 ==0:
        par.append(v)
    else:
        impar.append(v)
    if r =='N':
        break

print(f'A lista geral é {valores}')
print(f'A lista par é {par}')
print(f'A lista impar é {impar}')

