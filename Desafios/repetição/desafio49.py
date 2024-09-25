n=int(input('Digite um número para ver a tabuáda: '))
for c in range(1,11):
    s=c*n
    print('{} X {:.0f} = {:.0f}'.format(c,n,s))
