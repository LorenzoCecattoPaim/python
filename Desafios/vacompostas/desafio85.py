num=[[],[]]
valor=0
for n in range(1,8):
    valor=(int(input(f'Digite o {n}º número: ')))
    if valor %2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os números pares são {num[0]}')
print(f'Os números ímpares são {num[1]}')

