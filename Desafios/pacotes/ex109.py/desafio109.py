import moeda

p=int(input('Digite um preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'Com um aumento de 10% é = {moeda.aumentar(p,10,True)}')
print(f'Com um desconte de 13% é = {moeda.diminuir(p,13,True)}')