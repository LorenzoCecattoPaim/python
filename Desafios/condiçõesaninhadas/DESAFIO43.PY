preço=float(input('Qual o valor da compra? '))
print('''Escolha a forma de pagamento
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x cartão
      [4] 3x ou mais no cartão
      ''')
opição=int(input('Qual é a opição: '))
if opição==1:
    desconto=preço-(preço*10/100)
    print('A sua compra de {} no final vai custar {} com desconto'.format(preço,desconto))
elif opição==2:
    desconto=preço-(preço*5/100)
    print('A sua compra de {} no final vai custar {} com desconto'.format(preço,desconto))
elif opição	==3:
    parcela=preço/2
    print('As suas parcelas tem o valor de {} em 2x'.format(parcela))
    print('A sua compra de {} não terá alteração no preço'.format(preço))
elif opição ==4:
    quanpar=int(input('Quantas parcelas? '))
    juros=preço+(preço*20/100)
    parcela=juros/quanpar
    print('As suas parcelas tem o valor de {} em {}x'.format(parcela,quanpar))
    print('A sua compra de {} no final vai custar {} com JUROS'.format(preço,juros))
else:
    preço=0
    print('Opição inexistente, tente novamente')
