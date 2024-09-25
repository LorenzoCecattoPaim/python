maioridade=m=f20=0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    i=int(input('IDADE? '))
    s=input('SEXO?[M/F] ').upper()
    while s != 'M' and s !='F':
        s=input('SEXO?[M/F] ').upper()
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if i > 18:
        maioridade+=1
    if s =='M':
        m+=1
    if r=='N':
        break
    if s =='F' and i > 20:
        f20+=1
print('-'*20)
print('Fim do cadastro!')
print(f'''Tem {maioridade} pessoas com mais de 18 anos, {m} homens foram cadastrados 
      e {f20} são mulheres com mais de 20 anos''')