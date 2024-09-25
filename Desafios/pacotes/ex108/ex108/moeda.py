def dobro(pre):
    return pre*2

def metade(pre):
    return pre/2

def aumentar(pre,por=0):
    preço=(pre*por)/100+pre
    return preço

def diminuir(pre,porc=0):
    preçod=pre-(pre*porc)/100
    return preçod

def moeda(pre):
    Valor=f'R${pre:.0f},00'
    return Valor