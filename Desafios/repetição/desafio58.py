import random
numcom=random.randint(1,10)
adiv=int(input('Tente adivinhar o número de 1 a 10: '))
tentativas=1
while numcom !=adiv:
    print('Número errado, tente novamente!')
    adiv=int(input('Tente adivinhar o número de 1 a 10: '))
    tentativas+=1
print('Você ganhou!! Com {} tentativas'.format(tentativas))

