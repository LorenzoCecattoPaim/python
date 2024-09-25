def dobro(pre,mos=False):
    return pre*2 if mos == False else moeda(pre*2)

def metade(pre,mos=False):
    return pre/2 if mos == False else moeda(pre/2)

def aumentar(pre,por=0,mos=False):
    preço=(pre*por)/100+pre
    return preço if mos == False else moeda(preço)

def diminuir(pre,porc=0,mos=False):
    preçod=pre-(pre*porc)/100
    return preçod if mos == False else moeda(preçod)

def moeda(pre,mos=False):
    Valor=f'R${pre:.0f},00'
    return Valor


