r='S'
tot=0
soma=0
media=0
n=maior=menor=0
while r == 'S':
    n=int(input('Digite um número:  '))
    r=(input('Quer continuar?[S/N] ')).upper()
    soma+=n
    tot+=1
    if tot==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n < menor:
            menor=n

media=soma/tot
print('Você digitou {} numéros e a média deles é {}!!'.format(tot,media))
print('O maior número foi {} e o menor foi {}'.format(maior,menor))
