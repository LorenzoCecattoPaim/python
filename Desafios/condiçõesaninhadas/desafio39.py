import datetime
nas=int(input('Qual o ano de seu nascimento? '))
data=datetime.date.today().year
idade=(data)-(nas)
if idade>18:
    saldo=idade-18
    print('O tempo de alistamento já passou em {} anos'.format(saldo))
elif idade< 18:
    saldo=18-idade
    print('Você ainda tem que se alistar, em {} anos'.format(saldo))
elif idade == 18:
    print('Está na hora de se alistar')

