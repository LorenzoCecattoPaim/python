times=('Palmeiras','Corinthians','São Paulo','Red Bull Bragantino','Flamengo',
'Fluminense',
'Vasco da Gama',
'Botafogo',
'Cruzeiro',
'Atlético',
'Grêmio',
'Internacional',
'Athletico',
'Cuiabá',
'Bahia',
'Fortaleza',
'Vitória',
'Juventude',
'Criciúma', 
'Atlético-MG',)
print(f'Os times são {times}')
print(f'Os 5 primeiros times são :{times[:5]}')
print(f'Os 4 últimos são {times[16:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O juventude está na posição {times.index("Juventude")+1}')