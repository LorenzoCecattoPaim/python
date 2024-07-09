nome='Lorenzo Cecatto Paim'
email='emailverdadeiro@gmail.com'

#servidor
#print(email.find('@'))
servidor=email[16:]
print(servidor)

#primeiro nome do usurario
primeiro_nome=nome[:7]
print(primeiro_nome)

#mensagem
mensagem= f'usuário {primeiro_nome} cadastrado com sucesso com seu email {email}'
print(mensagem)

primeira_letra=email[0]
confirmação= f'enviamos uma mensagem de confirmação pra o email {primeira_letra}***{servidor}'
print(confirmação)