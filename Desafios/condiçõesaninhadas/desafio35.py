casa=float(input('Qual o valor da casa desejada? '))
salário=float(input('Qual é o seu salário? '))
anos=float(input('Em quantos anos você quer pagar a casa?'))
mensal= casa/(anos*12)
print('Para comprar a sua casa de {}R$ em {} anos'.format(casa,anos))
print('A mensalidade tem que ser de {}R$'.format(mensal))
if mensal > (salário*(30/100) + salário):
    print('Você não pode comprar esta casa! A prestação é de {} reais mensalmente'.format(mensal))
else:
    print('Empréstimo aprovado!')
