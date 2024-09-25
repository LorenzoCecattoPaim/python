time=[]
campeonato={}
gols=[]
while True:
    campeonato.clear()
    campeonato['nome']=input('Nome do Jogador: ')
    partidas=int(input(f'Quantas partidas {campeonato["nome"]} jogou? '))
    for p in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    campeonato['gols']=gols
    campeonato['total']=sum(gols)
    time.append(campeonato.copy())
    r=input('Quer continuar?[S/N] ').upper()
    while r != 'S' and r != 'N':
        r=input('Quer continuar?[S/N] ').upper()
    if r=='N':
        break



print('=-+'*10)
print(f'O jogador {campeonato["nome"]} jogou {partidas} partidas.')
for k,v in enumerate(campeonato['gols']):
    print(f'    ->Na partida {k}, fez {v} gols.')
print(f'Um total de {campeonato["total"]} gols')