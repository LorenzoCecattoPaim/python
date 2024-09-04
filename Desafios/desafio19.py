import random
n1=str(input('Digite um nome para sortear'))
n2=str(input('Digite um nome para sortear'))
n3=str(input('Digite um nome para sortear'))
n4=str(input('Digite um nome para sortear'))
lista=[n1,n2,n3,n4]
sort =random.choice(lista)
print(sort)