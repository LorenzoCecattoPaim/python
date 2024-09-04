import math
cateto1=float(input('Qual o valor do cateto adjacente?'))
cateto2=float(input('Qual o valor do cateto oposto'))
hipotenusa= (cateto1**2) + (cateto2**2)
print('A hipotenusa é {:.1f}'.format(math.sqrt(hipotenusa)))
