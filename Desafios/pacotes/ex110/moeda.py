def dobro(pre,mos=False):
    return pre*2 if mos == False else moeda(pre*2)

def metade(pre,mos=False):
    return pre/2 if mos == False else moeda(pre/2)
def moeda(pre,mos=False):
    Valor=f'R${pre:.0f},00'
    return Valor if mos == False else moeda(Valor)

def resumo(pre,aum,dim):
    print('='*30)
    print('     RESUMO DO VALOR')
    print('='*30)
    print('Preço analisado:',end='')
    print(f'{moeda(pre):>13}')
    print(f'O dobro do preço:',end='')
    print(f'{moeda(dobro(pre)):>13}')
    print(f'A metade do preço:',end='')
    print(f'{moeda(metade(pre)):>11}')
    print(f'{aum}% de aumento:',end='')
    print(f'{moeda((pre*aum)/100+pre):>14}')
    print(f'{dim}% de redução:',end='')
    print(f'{moeda(pre-(pre*dim)/100):>14}')
