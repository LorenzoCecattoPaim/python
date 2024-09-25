def ficha(g = 0 , nome='<Desconhecido>'):
    print(f'O jogador {nome} fez {g} gol(s) no campeonato.') 


nome=str(input('Nome: '))
gol=(input('Número de Gols: '))
if gol.isnumeric():
    gol=int(gol)
else:
    gol = 0
if nome.strip()== '':
    ficha(g=gol)
else:
    ficha(gol,nome)