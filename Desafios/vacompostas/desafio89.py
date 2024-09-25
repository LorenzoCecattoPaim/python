lista=[]
while True:
    nome=input('Nome:').capitalize()
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1,nota2], media])
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if r =='N':
        break
    
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i ,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('-'*35)
    opc=int(input('Quer ver a nota de qual aluno?(999 interrompe)'))

    if opc==999:
        print('--Fim do programa--')
        break
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]} ')
print('Volte sempre!!!') 