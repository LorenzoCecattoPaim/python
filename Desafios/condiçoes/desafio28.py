import random
numcom=random.randint(1,5)
adiv=int(input('Tente adivinhar o número de 0 a 5: '))
if numcom==adiv:
    print('Você ganhou!!')
else:
    print('Você perdeu, o número era {}'.format(numcom))

