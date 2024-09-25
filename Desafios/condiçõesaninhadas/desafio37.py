num=int(input('Digite um número inteiro: '))
print('''Escolha uma das opições de conversão:
      [1] para BINÁRIO
      [2] para OCTAL
      [3] para HEXADECIMAL
      ''')
opição=int(input('Sua opição: '))
if opição==1:
    print('O número {} em binário é {}'.format(num,bin(num)[2:]))
elif opição==2:
    print('O número {} em octal é {}'.format(num,oct(num)[2:]))
elif opição==3:
    print('O número {} em Hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Opição inválida!')