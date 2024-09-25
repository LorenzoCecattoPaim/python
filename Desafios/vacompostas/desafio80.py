números=[]
for c in range(0,5):
    n=int(input(f'Digite um número: '))
    if c == 0 or n > números[-1]:
        números.append(n)
        print('Valor adicionado no fim da lista!')
    else:
        pos=0
        while pos < len(números):
            if n <= números[pos]:
                números.insert(pos,n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos+=1
print(f'Os valores digitados em ordem foram {números}')