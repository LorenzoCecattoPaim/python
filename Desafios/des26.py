frase=str(input('Digite uma frase')).strip()
frase=frase.lower()
quant=frase.count('a')
prim=frase.find('a')+1
ult=frase.rfind('a')+1
print('A frase tem {} letras a, a primeira está na posição {} e o último na posição {}'.format(quant,prim,prim))