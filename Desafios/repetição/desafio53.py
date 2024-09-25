f = str(input('Digite uma frase para ver se é um palíndromo: ').strip().upper())
palavras= f.split()
junto=''.join(palavras)
inverso=''
for i in range(len(junto)-1,-1,-1):
    inverso +=junto[i]
    #print(junto[i], end='')
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')