from random import randint
lista=[]
jogos=[]

print('-'*30)
print('      JOGO DA MEGACENA      ')
print('-'*30)
quant=int(input('Quantos jogos quer que eu sorteie? '))
tot=1
while tot <= quant:
    cont=0    
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*20)
print(f'Sorteando {quant} jogos')
for c,l in enumerate(jogos):
    print(f'JOGO {c+1} : {l}')
