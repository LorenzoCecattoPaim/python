nome=str(input('Qual o seu nome completo?'))
mai=nome.upper()
minu=nome.lower()
pri=nome.split()
nome.strip()
prime=len(pri[0])
jun=''.join(pri)
junto=len(jun)
print('Seu nome em maíusculo é {}, em minúsculo {}, ao todo tem {} letras e o primeiro nome tem {} letras'.format(mai,minu,junto,prime))