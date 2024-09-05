anoa=int(input('Digite o ano que você quer saber: '))
if anoa > 1900 and anoa%4==0:
    print('O ano {} é bissexto'.format(anoa))
else:
    print('O ano {} não é bissexto'.format(anoa))