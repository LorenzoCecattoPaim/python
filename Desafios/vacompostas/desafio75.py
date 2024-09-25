
numeros=(int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite  mais um número: ')),
         int(input('Digite algum número: ')))
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O três aparece na posição {numeros.index(3)+1}')
else:
    print('O 3 não foi digitado')
print('Os valores pares digitados foram ',end='')
for p in numeros:
    if p % 2 ==0:
        print(p, end=' ')

