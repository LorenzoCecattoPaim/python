import random

numeros_sorteados = [random.randint(1, 100) for _ in range(5)]
print(f'Os números sorteados são: {numeros_sorteados}')
tamanho=sorted(numeros_sorteados)
print(f'O maior número é {tamanho[-1]} e o menor é {tamanho[0]}')
