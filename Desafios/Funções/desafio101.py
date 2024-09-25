
def votar(nas):
    import datetime
    
    data=datetime.date.today().year
    idade=(data)-(nas)

    if  16 <= idade < 18 or idade >= 60:
        return f"Com {idade} o voto é OPICIONAL!"
    elif idade < 16:
        return f"Com {idade} NÃO VOTA!"
    else:
        return f"Com {idade} o voto é OBRIGATÓRIO!"


nas=int(input('Qual o ano de seu nascimento? '))
print(votar(nas))