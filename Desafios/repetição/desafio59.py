n1=int(input('Digite o 1º valor: '))
n2=int(input('Digite o 2º valor: '))
maior=0

print('''
      Escolha alguma opição:
      [ 1 ] SOMAR
      [ 2 ] MULTIPLICAR
      [ 3 ] MAIOR
      [ 4 ] NOVOS NÚMEROS
      [ 5 ] SAIR DO PROGRAMA
      ''')
opição=int(input('Qual a sua opição? '))
while opição != 5:
    if opição == 1:
        print('----------A soma do número {} com {} é {}-----------'.format(n1,n2,n1+n2))
        print('''
            Escolha alguma opição:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA
      ''')
        opição=int(input('Qual a sua opição? '))
    elif opição == 2:
        print('----------A multiplicação do número {} com {} é {}-----------'.format(n1,n2,n1*n2))
        print('''
            Escolha alguma opição:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA
      ''')
        opição=int(input('Qual a sua opição? '))
    elif opição==3:
        if n1 > n2:
            maior=n1
        else:
            maior=n2
        print('-----------O maior número é {}-----------'.format(maior))
        print('''
            Escolha alguma opição:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA
      ''')
        opição=int(input('Qual a sua opição? '))
    elif opição==4:
        print('-----------Digite os outros valores-----------')
        n1=int(input('Digite o 1º valor: '))
        n2=int(input('Digite o 2º valor: '))
        print('''
            Escolha alguma opição:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA
      ''')
        opição=int(input('Qual a sua opição? '))
    else:
        print('-----------Opição inválida-----------')
        print('''
            Escolha alguma opição:
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEROS
            [ 5 ] SAIR DO PROGRAMA
      ''')
        opição=int(input('Digite novamente outra opição: '))
print('-----------Fim do menu!!!-----------')