dis=float(input('Qual é a distância de sua viagem em Km? '))
if dis>200:
    preço=dis*0.50
else:
    preço=dis*0.45
print('O preço da passagem é {} reais'. format(preço))