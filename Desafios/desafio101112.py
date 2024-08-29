#Preço=float(input('Qual é o preço do produto'))
#aumento=int(input('Qual é a porcentagem do aumento?'))
#print('O preço vai ser de {} com {}%'.format((Preço*aumento/100)+Preço , aumento))

dia=int(input('Quantos dias com o carro alugado?'))
km=float(input('Quantos km rodados? '))
print('Você deverá pagar ${} por {} rodados e {} dias'.format((dia*60)+(km*0.15), km , dia))