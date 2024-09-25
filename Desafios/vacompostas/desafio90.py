
aluno={

}
aluno['nome']=input('Qual o nome do aluno? ').capitalize()
aluno['média']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] > 7:
    aluno['situação']='Aprovado'
elif aluno['média'] > 5:
    aluno['situação']='Recuperação'
else:
    aluno['situação']='Reprovado'

for k,v in aluno.items():
    print(f'{k} é igual  a {v}')