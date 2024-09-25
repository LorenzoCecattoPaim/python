def leiaint(msg):
    ok=False
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Informe um valor inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada interrompida!')
            return 0
        else: 
            return n

def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Informe um valor real válido!')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada interrompida!')
            return 0
        else: 
            return n
n=leiaint('Digite um número: ')
n2=leiafloat('Digite um num real: ')
print(f'Você digitou o número inteiro {n} e o real foi {n2}')