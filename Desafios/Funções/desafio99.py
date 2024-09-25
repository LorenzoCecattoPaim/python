def maior(* num):
    cont=maior=0
    print('-='*20)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        if cont == 0:
            maior= n
        if n > maior:
            maior=n
        cont+=1
    print(f'Foram passados {len(num)} valores ao total.')
    print(f'O maior valor é o {maior}') 
    cont+=1
maior(4,5,1)
maior(2,1,7,3)
maior(2,10,4,8)