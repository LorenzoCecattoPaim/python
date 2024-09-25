import moeda

p=int(input('Digite um preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Com um aumento de 10% é = {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Com um desconte de 13% é = {moeda.moeda(moeda.diminuir(p,13))}')



