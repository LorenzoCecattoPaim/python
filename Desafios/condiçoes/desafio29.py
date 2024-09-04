velo=int(input('Qual a velocidade do carro? '))
max=80
if velo>max:
    print('Você foi multado')
    print('O valor da multa é de {} reais'.format((velo-max)*7))
else:
    print('Tudo certo!')