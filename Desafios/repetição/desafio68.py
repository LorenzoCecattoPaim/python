from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*20)
computador=randint(1,10)
n=c=s=0
while True:
    n=int(input('Digite um valor: '))
    e=str(input('Par ou Ímpar?[P/I] ')).upper()
    s=n+computador
    print('-'*20)
    print(f'Você jogou {n} e o computar {computador}. Total de {s}. ',end='')
    if e == 'P' and s%2==0:
        print('DEU PAR')
        print('JOGADOR VENCEU!!!')
        print('=-'*20)
        print('Vamos continuar!')
        c+=1
    elif e == 'I' and s%2!=0:
        print('DEU ÍMPAR')
        print('JOGADOR VENCEU!!!')
        print('=-'*20)
        print('Vamos continuar!')
        c+=1
    else:
        print('Você PERDEU!')
        break
print('=-'*20)
print(f'GAME OVER!Você venceu {c} vezes')



