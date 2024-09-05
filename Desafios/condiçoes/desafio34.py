sal=float(input('Qual o seu salário atual?'))
if sal >=1250:
    sal= sal*(10/100)+sal
if sal <1250:
    sal =sal*(15/100)+sal
print('O seu salário com aumento é de {} reais'.format(sal))