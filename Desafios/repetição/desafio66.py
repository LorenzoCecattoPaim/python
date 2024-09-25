s=c=n=0
while True:
    n=int(input('Digite um número [999 PARA]: '))
    if n == 999:
        break
    c += 1
    s += n

print(f'Você digitou {c} números e a soma deles é {s}')