import datetime
nas=int(input('Qual o ano de seu nascimento? '))
data=datetime.date.today().year
idade=(data)-(nas)
if idade <9:
    print('Você é mirim')
elif idade <14:
    print('Você é infantil')
elif idade <19:
    print('Você é júnior')
elif idade <20:
    print('Você é sênior')
elif idade >20:
    print('Você é MASTER')