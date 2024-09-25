import moeda

p=int(input('Digite um preço: R$'))
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'Com um aumento de 10% é = {moeda.aumentar(p,10)}')
print(f'Com um desconte de 13% é = {moeda.diminuir(p,13)}')



