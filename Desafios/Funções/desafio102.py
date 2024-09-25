def fatorial(n,show=True):
    """
    ->Calcula o FATORIAL de um número
    :param n: O número a ser calculado o fatorial!
    :param show: (Opicional) Mostrar ou não a multiplicação
    :return: O valor do Fatorial de um número n.
    """


    f=1
    for c in range(n,0,-1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5,show=True))
help(fatorial)