import random
import time
def sort(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for cont in range(0,5):
        n=random.randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        time.sleep(0.4)
    print('PRONTO!')

def somapar(lista):
    soma=0
    for c in lista:
        if c % 2 ==0:
            soma+=c
    print(f'A soma dos números pares da lista é {soma}')
números=[]
sort(números)
somapar(números)