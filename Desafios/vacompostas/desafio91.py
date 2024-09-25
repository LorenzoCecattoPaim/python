from random import randint
import time
from operator import itemgetter
jogo={
'Jogador-1':randint(1,6),
'Jogador-2':randint(1,6),
'Jogador-3':randint(1,6),
'Jogador-4':randint(1,6)
}
ranking=[]
for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    time.sleep(1)
print('=+='*10)
print('---------Resultados:---------')
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'    O {i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)