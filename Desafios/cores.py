cores={
    'Amarelo':'\033[33m',
    'Azul':'\033[34;41m',
    'Verde':'\033[32m',
    'limpa':'\033[m',
    'Vermelho':'\033[31m',
    'Cinza':'\033[37m',
    'Ciano':'\033[36m',
    'roxo':'\033[35m',
}
nome=str(input('Qual é o seu nome? '))
print('{}{}{} é lindo(a)'.format(cores['Azul'],nome,cores['limpa']))