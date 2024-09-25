import datetime
trabalho={
}
trabalho['nome']=input('Nome: ').capitalize()
nas=int(input('Ano de Nascimento: '))
data=datetime.date.today().year
trabalho['idade']=(data)-(nas)
trabalho['ctps']=int(input('Carteira de Trabalho(0 se não tem): '))
if trabalho['ctps'] != 0:
    trabalho['contratação']=int(input('Ano de Contratação?'))
    trabalho['salário']=input('Salário: R$')
    trabalho['aposentadoria']=(trabalho['contratação']-nas)+35
for k,v in trabalho.items():
    print(f'    -{k} tem o valor de {v}')