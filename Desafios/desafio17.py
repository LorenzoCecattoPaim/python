import math
an=float(input('Digite um ângulo: '))
seno=math.sin(math.radians(an))
cosseno=math.cos(math.radians(an))
tangente=math.tan(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}, o seno de {:.2f} e a tangente de {:.2f}'.format(an,cosseno,seno,tangente))