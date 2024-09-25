n=c=0
while True:
    n=int(input('Digite um número para ver a tabuáda: '))
    if n<0:
        break

    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
print('FIM DO PROGRAMA DE TABUÁDA!!! Volte sempre')
    